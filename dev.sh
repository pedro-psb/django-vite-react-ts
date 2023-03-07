#!/bin/bash
# run dev server for django and vite
# ref: https://how-to.dev/how-to-create-tmux-session-with-a-script

# Launches vite and manage.py runserver inside tmux
function run-servers(){
  session="django-vite"
  run_vite="npm run dev"
  run_django="source .venv/bin/activate && python3 manage.py runserver"
  # run_vite="echo hola"
  # run_django="echo hola-again"

  tmux kill-server
  # tmux kill-session $session

  tmux new-session -d -s $session
  tmux rename-window -t $session:1 'vite'
  tmux send-keys -t $session:1 "$run_vite" Enter
  tmux split-window -h
  tmux send-keys -t $session:1 "$run_django" Enter

  tmux attach-session -t $session
}

run-servers

