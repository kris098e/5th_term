#!/bin/bash
find . -name '*.png' ! -path './5th_term/pictures/*' -exec mv {} 5th_term/pictures/ \;
