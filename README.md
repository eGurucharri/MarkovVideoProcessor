### About MVP

MarkoVideoProcessor is a simple program that takes several videos from a folder, extracts a random segment from each, and repeats the process until the total duration set by the user is reached.

At its core, it's a hobby project. The idea came to me while experimenting with another small program based on Markov chains, which I humorously named “Dzyga_Markov” as a nod to filmmaker Dziga Vertov. Through that playful connection, I asked myself, “What if I applied the concept of Markov chains to video?” From there, I built a simple prototype using Vertov’s *Kino-Pravda* reels. The results exceeded my expectations, reminding me of the concept of "automatic writing" that artists like Jim Morrison or the infamous Enrique Bunbury often boasted about. Kinda like dadaist stuff, also.

### How to Use It

Currently, the program probably only works on Linux, and it's not the most user-friendly application just yet. Here’s how to use it:

1. Clone the repository.
2. Ensure that **ffmpeg** is installed.
3. Install the required dependencies.
4. Add some videos (preferably in `.mp4` format) to the “videos” folder, or alternatively, select another folder from the GUI.
5. Activate the virtual environment and run `main.py` (or simply run everything from PyCharm).
6. Choose your desired options, such as the duration (most tests have been done with 60-second outputs), filters, speed effects, and the output video name.
7. Click the **Generate Video** button.
8. Wait for the video to process.
9. The final video will appear in the “outputs” folder.

### Roadmap

For more detailed insights, check the **Issues** section in the repository. My primary goal for the first official version is to ensure compatibility across major operating systems (Windows and macOS), while addressing the most critical bugs. Another critical goal is to add support to more video formats.