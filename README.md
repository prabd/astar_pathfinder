<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
    * [Starting the Visualizer](#starting-the-visualizer)
    * [Specifying Parameters](#specifying-parameters)
* [Roadmap](#roadmap)
* [License](#license)
* [Contact](#contact)


<!-- ABOUT THE PROJECT -->
## About The Project

[![Screenshot][final-screenshot]](https://github.com/prabd/astar_pathfinder)

I made this little program just for fun and as a warmup for Python. We had recently covered graph traversals in class, such as depth-first search (DFS) and breadth-first search (BFS), and I wanted to look at other pathfinding algorithms. One algorithm I found was the A* algorithm, which doesn't give the optimal path, but a solution that's pretty close (i.e. it's a heuristic algorithm). However, A* is much more time efficient than BFS/DFS.

Implementing the algorithm is pretty straightforward, but I also wanted to play with some Python libraries like Pygame, which is why I added a visualizer. 


<!-- GETTING STARTED -->
## Getting Started
To get a local copy up and running on Linux follow these simple steps.

### Prerequisites
This program only uses Pygame as an external library, so check to make sure that is installed.

If it is not installed, you can run the following in a terminal to install it:
```sh
python3 -m pip install pygame
```


### Installation

1. Clone the repo
```sh
git clone https://github.com/prabd/astar_pathfinder.git
```
2. Navigate into the directory
```sh
cd astar_pathfinder/
```


<!-- USAGE EXAMPLES -->
## Usage

### Starting the Visualizer

```sh
python3 astar.py
```

### Specifying Parameters
When the program starts, it'll ask for a couple search parameters in the terminal. After user enters the parameters, a screen will pop up.

Here, the user can select obstacles (or walls) by holding down click and moving over the squares, which will turn `black`. This signifies that the algorithm will consider that square as impossible to traverse.

Once the user is done selecting, press `enter` to begin the pathfinder.
As the algorithm runs, squares will be `dark gray` if closed, `red` if enqueued, and `blue` if currently being considered.


If a path is found, the path will be shown in `blue`.

<!-- ROADMAP -->
## Roadmap

Possible Future Improvements
* Better error handling
* Add GUI for selecting parameters instead of specifying via terminal
* Add GUI for clearing obstacles and restarting the process.
* Implement and add other algorithms to choose from.


<!-- LICENSE -->
## License

Distributed under the MIT License.

<!-- CONTACT -->
## Contact

Prab Dhaliwal - prabd62@gmail.com

Project Link: [https://github.com/prabd/astar_pathfinder](https://github.com/prabd/astar_pathfinder)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/badge/contributors-1-green.svg
[contributors-url]: https://shields.io/
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=flat-square
[license-url]: https://github.com/prabd/astar_pathfinder
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/prab-dhaliwal-1603531a0
[initial-screenshot]: images/initial.png
[final-screenshot]: images/final.png
[obstacles-screenshot]: images/obstacles.png
[terminal-screenshot]: images/terminal.png
