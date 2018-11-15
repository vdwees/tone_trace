import os
import sys
from contextlib import contextmanager
from trace import Trace

from .key_mappings import translate_to_note

# Some submodules can be very noisy. We keep them silent with this wrapper
@contextmanager
def silence_stdout():
    new_target = open(os.devnull, "w")
    old_target, sys.stdout = sys.stdout, new_target
    try:
        yield new_target
    finally:
        sys.stdout = old_target


class ToneTrace(Trace):
    def __init__(self, *args, **kwargs):
        self.step_into = kwargs.pop("step_into", False)
        self.line_number_sequence = []
        self.base_file = None
        super().__init__(*args, **kwargs)

    def localtrace_trace(self, frame, why, arg):
        if why == "line":
            # The first line will always be the base_file
            if self.base_file is None:
                self.base_file = frame.f_code.co_filename

            # TODO: Naming collisions between the base file and traced files is
            # possible. Should figure out how to not trace any other files.
            if frame.f_code.co_filename == self.base_file:
                # Record the line if it is at the top level file
                self.line_number_sequence.append(frame.f_lineno)
                print("^ Added!")
            elif self.step_into:
                # Also record the lines that were stepped into
                self.line_number_sequence.append(frame.f_lineno)
                print("^ Added!")

        return super().localtrace_trace(frame, why, arg)


def main():
    import argparse
    from .PySynth.pysynth import make_wav
    import simpleaudio as sa

    parser = argparse.ArgumentParser()

    parser.add_argument("filename", help="File to play", type=str)
    parser.add_argument(
        "-s",
        "--step_into",
        action="store_true",
        help="Record all referenced files as well",
        default=False,
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Dump all tracing info",
        default=False,
    )
    parser.add_argument(
        "-p",
        "--play",
        action="store_true",
        help="Play outputfile afterword",
        default=False,
    )

    opts = parser.parse_args()

    if opts.filename is None:
        parser.error("Filename is missing: nothing to play")

    sys.path[0] = os.path.dirname(opts.filename)

    ttrace = ToneTrace(count=0, trace=1, step_into=opts.step_into)
    try:
        with open(opts.filename) as fp:
            code = compile(fp.read(), opts.filename, "exec")
        # Try to emulate __main__ namespace as much as possible
        globs = {
            "__file__": opts.filename,
            "__name__": "__main__",
            "__package__": None,
            "__cached__": None,
        }

        # Run a trace, recording line numbers
        if not opts.verbose:
            with silence_stdout():
                ttrace.runctx(code, globs, globs)
        else:
            ttrace.runctx(code, globs, globs)

        # Translate line numbers into pysynth-style notes
        notes = [translate_to_note(line) for line in ttrace.line_number_sequence]

        # Make a .wav file of results
        print("Processing Results")
        outfile = opts.filename.replace(".py", ".wav")
        make_wav(notes, bpm=500, fn=outfile)

        # Play the output file directly
        if opts.play:
            wave_obj = sa.WaveObject.from_wave_file(outfile)
            play_obj = wave_obj.play()
            play_obj.wait_done()

    except OSError as err:
        sys.exit("Cannot run file %r because: %s" % (sys.argv[0], err))
    except SystemExit:
        pass


if __name__ == "__main__":
    main()
