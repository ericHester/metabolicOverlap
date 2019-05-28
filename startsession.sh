#!Source me
. ./.local/bin/activate
export PATH="`echo $PATH|sed 's/\([^\\]\) /\1\\\\ /g'`" #Handle spaces in PATH

export ModelSEEDDatabase="$PWD/sourcedata/ModelSEEDDatabase"

