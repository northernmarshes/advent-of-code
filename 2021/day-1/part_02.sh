#!/usr/bin/env bash

# mapfile -t ARR <sample.txt
mapfile -t ARR <input.txt

make_new_array ()
{
    local ARR1=$1
    local INDEX2=1
    local INDEX2=2
    for LINE in "$ARR1[@]"; do
      NEXT1="${ARR["$INDEX1"]}
      NEXT2="${ARR["$INDEX2"]}
      ARR2+="$(($INCREASED + $NEXT1 + $NEXT2))"
      INDEX1="$(($INDEX + 1))"
      INDEX2="$(($INDEX + 1))"
    done
    return ARR2
}

ARR=(make_new_array ARR)

INDEX=-1
INCREASED=0

for LINE in "${ARR[@]}"; do
  PREVIOUS="${ARR["$INDEX"]}"
  echo "Previous: $PREVIOUS"
  echo "Current: $LINE"
  if [ $LINE -gt $PREVIOUS ]; then
    echo "Increased"
    INCREASED="$(($INCREASED + 1))"
  else
    echo "Decreased"
  fi
  INDEX="$(($INDEX + 1))"
done

echo "Increased $INCREASED times."
