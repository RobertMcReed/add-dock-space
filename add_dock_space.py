"""Add a single blank space to the macOS dock."""

from os import system

system("defaults write com.apple.dock persistent-apps -array-add '{\"tile-type\"=\"spacer-tile\";}'; killall Dock")
