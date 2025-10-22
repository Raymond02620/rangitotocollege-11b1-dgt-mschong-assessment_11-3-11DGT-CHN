from tkinter import *
import tkinter as tk
import random
import json
import sys
import subprocess
import os

if not os.path.exists('Python/rps'): # Create saves directory if it doesn't exist
    os.makedirs('Python/rps') # Create the directory