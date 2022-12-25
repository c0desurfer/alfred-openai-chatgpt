query=${1}

if command -v pyenv 1>/dev/null 2>&1
then

  export PYENV_ROOT="$HOME/.pyenv"
  export PATH="$PYENV_ROOT/bin:$PATH"

  export PYENV_VIRTUALENV_DISABLE_PROMPT=1

  eval "$(pyenv init --path)"
  eval "$(pyenv init -)"
  eval "$(pyenv virtualenv-init -)"
  pyenv activate ${pyenv}
fi

${python} openai_workflow.py ${api_key} ${max_tokens} ${query}