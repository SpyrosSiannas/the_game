#!/bin/bash

python=python3
pip=pip3

if [ ! -d env ]; then
    $python -m venv env
    source env/bin/activate
    $python -m pip install --upgrade pip
    $pip install -r requirements.txt
else
    source env/bin/activate
fi


while [[ $# -gt 0 ]]; do
  case $1 in
    --ball)
      GAME="examples/ball_example.py"
      shift # past argument
      shift # past value
      ;;
    --pong)
      GAME="examples/pong_example.py"
      shift #past argument
      shift #past value
      ;;
    -m|--main)
      GAME="main.py"
      shift # past argument
      shift # past value
      ;;
    --default)
      GAME="main.py"
      shift # past argument
      ;;
    -*|--*)
      echo "Unknown option $1"
      exit 1
      ;;
  esac
done

$python $GAME
