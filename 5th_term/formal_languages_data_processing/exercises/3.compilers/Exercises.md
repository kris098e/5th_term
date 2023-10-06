Exercises

In preparation for the class, you should download and test SCIL, so you know if you encounter any problems. To run it, you need python3 and the ply package. If you don't have the package, you can install it with `pip3 install ply`. If you don't have `pip3`, you need to install that first, but Ubuntu (possibly linux via WSL) or your Mac should suggest how to do that.

1. Consider the [visitor example](https://imada.sdu.dk/u/kslarsen/dm565/Files/VisitorExample/) and explain why, in `LeavesVisitor`, it is OK to omit code for `Node`, and why recursive traversal through the `Node`s still take place. Make a `PrettyPrintVisitor` where you use indentation in some way you define yourself to print the entire tree in a form where one can graphically identify the subtrees. The purpose of this exercise is to explain visitor patterns, which are used in the SCIL compiler, in a simpler setting.
	1. Because we don't care about the nodes. It does not break since it does not find a function for other things than a leaf
	2. It still takes place, since we still call the `accept()` on the left and right child if they are there.
	3. Make the new `PrettyPrintVisitor` class, have a global variable and indent one more each time we print.
2. Resolve possible problems with downloading and running SCIL.
	1. 
3. Get a feeling for the syntax of SCIL just by looking at a few programs in the Test directory. Write a program with two functions, both with one argument, n. One function should iteratively add the numbers from 1 through n, and the other should obtain the same recursively. Print the two results for confirmation. ツ
	1. follow the instructions of what is allowed 
4. Make changes in lexer_parser.py:
    1. Allow the user to choose between using the keyword `while` and the keyword `as_long_as`.
	    1. 
    2. Change the end-of-statement symbol from semicolon to period.
    3. Allow vertical lines for line-up, so this is a legal program:
        
        while i < 10 do {
        |  s = s + i;
        |  i = i + 1;
        |  if i == 10 then {
        |  |  print 42;
        |  } else {
        |  |  dummy = 0;
        |  }
        }
        
        You are not supposed to check that the user uses the line-up in any particular way; you just have to allow the symbol. Note that an if-statement must include an else-part.
    4. Explain what happens if the line
        t.lexer.lineno += t.value.count("\n")
        is changed to
        t.lexer.lineno += 1
	        - it would give incorrect values on which line number things are happening on
        
5. Define the following three regular expressions:
    1. Numbers in scientific notation (E-notation).
	    1. `(+|-)?[[:digit:]]\.[[:digit:]]+E[\+-]?[[:digit:]]+`
    2. URLs (it is OK that your expression matches some reasonable superset of what is allowed).
	    1. `http(s)?://(www\.)[[:alanum:]]+\.(com|dk|se|...)(/[[:alpha:]])*`
    3. Strings as in normal programming languages, _including_ the beginning and ending double quotes (it is OK that backslashed double quotes are _not_ allowed inside the strings).
	    1. `"[^"']"`
6. Make and test the following four Flex scanners:
    1. Make texts (more) politically correct by replacing "idiot" with "intellectually challenged person", etc.
	```java
	%{
		C definition
	}%
	%option noyywrap
	
	%%
	"idiot" { printf(intellectually challenged person); }
	.       { prinft("%s", yytext)}

	%%
	void main() {
		yylex():
	}	
	```

    3. Remove all whitespace and produce lines in lengths of 80 characters.
![[Pasted image 20231006123040.png]]
matching on new line or space we dont do anything.
Else we start counting, and print each character whenever we see it.

4. Replace all sequences of whitespace with one blank and produce lines as long as possible, but at most 80 characters, by dividing only at blanks (that is, between words).
![[Pasted image 20231006123233.png]]
5. Remove all tags from an HTML document. For those who do not speak HTML fluently, HTML is just regular text with some extra interpreted constructions. A _tag_ consists of a "less than" symbol followed by some text and closed by a "greater than" symbol, or it might have slash after the "less than" symbol (you can view the source of this page to see an example).
![[Pasted image 20231006124105.png]]
Matching on an html tag we will not do anything. Matching on anything else  we print it
1. Appel 2.9. Just draw the DFA and mark final states with the action (1, 2, or 3) that should be taken.
![[Pasted image 20231006125134.png]]
Make a DFA for each, then make it to an NFA, and then convert it to a DFA.

Since 1 and  overlaps, the accept state of the DFA will have two actions to choose from. Choose this i a prioritized manner, and take the regex which is prioritized highest.
![[2-9.jpeg]]