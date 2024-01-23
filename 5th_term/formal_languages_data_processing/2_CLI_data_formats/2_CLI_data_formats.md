[[04.pdf]]
[[05.pdf]]
# Data formats
## Tabular data formats
Difference in the seperation

has specific rules to fx the `header`, same number of `comma seperated fields`, what should be `escaped` 
### tsv
tab-seperated
### csv
comma-seperated
### sql and xlxs files
can be exported with build in features

## JSON
JavaScript Object Notation
## XML
eXtensible Markup Language
![[Pasted image 20230920093752.png]]

# Data discovery
done in an **incremental** fashion, i.e do something and see what it does, then `pipe` it to the next command
Also done since we dont want to write to disc before we are done with the entire process

**learning by doing**

# Pitfalls
Character ascii encoding
- Different encoding in different systems
Have to be aware of this to not make mistakes on some assumptions
# CLI Tools
- wc (word count)
- file (determine file type)
- recode (recode file to different format)
- od (octal dump)
- od -tcuC
- grep
- sed
- gawk
- sort
- uniq
	- Used after sorting as it is inefficient
- tr
	- translates characters into another character. Is not line oriented
	- can also delete specific characters
- cut
	- cut out some columns
- paste
	- Merge lines of files, i.e using 2 or more files
- join
	- join lines on common field in 2 files
	- Like natural join in databases
- head/tail
	- output first/last lines in file
## grep
using `-E` interprets  special characters without using escape on it
use `^` to negate the expression, but has to be inside of a special operator
there are also predefined expressions which can be used

Has options for ignoring case, printing the lines that does not matches the regex ...
### Syntax
1. **Quantifiers**:
    - `*`: Matches zero or more occurrences of the preceding element.
	- `+`: Matches one or more occurrences of the preceding element.
    - `?`: Matches zero or one occurrence of the preceding element.
    - `{n}`: Matches exactly `n` occurrences of the preceding element.
    - `{n,}`: Matches `n` or more occurrences of the preceding element.
    - `{n,m}`: Matches between `n` and `m` occurrences of the preceding element.

2. **Flags**:
    - `i`: Case-insensitive matching.
    - `g`: Global matching (find all matches, not just the first one).
    - `m`: Multiline matching.

3. **Named capture groups**:
    - `(?<name>...)`: Defines a named capture group.
    - Example: `/Testing (?<num>\d{3})/`

4. **Using parentheses**:
    - Parentheses `( )` are used to group parts of the regex and create capture groups.
    - Captured substrings can be referenced later or used for replacements.
    - Example: `(This) is \1 power`
5. **References**
	1. `\1` fx matches the first group matching. `\2` ofc matches the 2nd group
## sed
More powerful tool, stream-oriented

Has to have the given syntax given below
first given an address to start from then `,` another address **which can be a regular expression**
![[05.pdf#page=12]]
You can also provide options, `see man page`
### Substitute
useful operation / command. Can use regular expressions
#### Examples
see slides
## awk
Complete programming language
Complicated

