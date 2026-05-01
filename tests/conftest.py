import sys
import os

# Ensure the project src/ directory is on sys.path for tests in CI
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
