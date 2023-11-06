<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-type" content="text/html; charset=utf-8" />
<meta name="viewport" content="width=device-width">
<meta name="Author" content="Kim Skak Larsen" />
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<link rel="stylesheet" type="text/css" href="design.css?v=1.1">
<title>DM565 - Formal Languages and Data Processing</title>
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js">
</script>

</head>
<body>

<script>
/* For small screens, menu gets packed */
function myPhoneMenu() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}

/* The following is only relevant for large screens, but shouldn't hurt */
    
/* For buttons, toggle between hiding and showing the dropdown content */
function myMenuSelector(elmnt) {
    ident = elmnt.parentElement.children[1].id;
    elmnt.parentElement.children[1].classList.toggle("show");
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (!elmnt.parentElement.contains(openDropdown) && openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
}

/* Close the dropdown if the user clicks outside of it */
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {

    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}
</script>

    
<div id="main">
<a id="undecorated" href="index.php">

<table width="100%">

<tr><td>
<table>
<tr><td>
<div id="coursetitle">DM565 - Formal Languages and Data Processing</div>
</td></tr>
<tr><td>
    &nbsp;
</td></tr>
<tr><td>
Fall 2023
</td></tr>
<tr><td>
<b>Kim Skak Larsen</b>
</td></tr>
</table>
</td>

<td>
<img id="logo" src="IMADA_en.png" alt="[topimage]" align="right"/>
</td>
</tr>

</table>

</a>
<noscript>
   &nbsp; JavaScript skal være slået til for at denne side virker.
</noscript>

<hr>
      
<div class="topnav" id="myTopnav">
  <a href="index.php" class="active">Home</a>
  <div class="dropdown">
    <button class="dropbtn" onclick="myMenuSelector(this)">Signing-Up
      <i class="fa fa-caret-down"></i>
    </button>
    <div class="dropdown-content">
      <a href="https://odin.sdu.dk/sitecore/index.php?a=fagbesk&id=119336&listid=1755&lang=en" target="_blank">Official Course Description</a>
      <a href="language.php">Language Policy</a>
      <a href="eval-final-res.pdf" target="_blank">Latest Evaluation (course part) [2023]</a>
      <a href="eval_inno.pdf" target="_blank">Latest Evaluation (innovation) [2021]</a>
      <a href="handlingsplan-dm565-2019.pdf" target="_blank">Latest Plan of Action [2019]</a>
      <a href="histogram.php">Latest Exam Results [2022]</a>
    </div>
  </div> 
  <div class="dropdown">
    <button class="dropbtn" onclick="myMenuSelector(this)">Material
      <i class="fa fa-caret-down"></i>
    </button>
    <div class="dropdown-content">
      <a href="notes.php">Lectures and Exercises</a>
      <a href="literature.php">Literature</a>
      <a href="scil.php">SCIL</a>
    </div>
  </div> 
  <div class="dropdown">
    <button class="dropbtn" onclick="myMenuSelector(this)">Exam
      <i class="fa fa-caret-down"></i>
    </button>
    <div class="dropdown-content">
      <a href="exam.php">Exam</a>
      <a href="reexam.php">Reexam</a>
      <a href="questions.php">Curriculum</a>
<!--      <a href="faq.php">FAQ</a> -->
    </div>
  </div> 
  <div class="dropdown">
    <button class="dropbtn" onclick="myMenuSelector(this)">Contact
      <i class="fa fa-caret-down"></i>
    </button>
    <div class="dropdown-content">
      <a href="schedule.php">Schedule</a>
      <a href="contact.php">Contact Information</a>
      <a href="tas.php">Teaching Assistants</a>
    </div>
  </div> 
  <a href="innovation.php" class="active">Innovation</a>
  <!--<a href="corona.php" class="active">Corona</a>-->
  <a href="javascript:void(0);" style="font-size:15px;" class="icon" onclick="myPhoneMenu()">&#9776;</a>

</div>

<hr>
      
<div id="content">

<div id="page-headline">Exercises</div>

<ol>
<li>
Consider the files
<ul>
<li><a href="Files/File_Ex_UTF8.txt">File_Ex_UTF8.txt</a>
</li>
<li><a href="Files/File_Ex_Latin1.txt">File_Ex_Latin1.txt</a>
</li>
<li><a href="Files/File_Ex_Unix_Eol.txt">File_Ex_Unix_Eol.txt</a>
</li>
<li><a href="Files/File_Ex_MS-DOS_Eol.txt">File_Ex_MS-DOS_Eol.txt</a>
</li>
</ul>
Use the command-line possibilities to inspect these files, i.e., what
does <code>file</code> and <code>wc</code> say about them? Inspect
them using <code>od</code> with appropriate options; start with
<code>od -tcuC</code>, for instance. How do they
differ? Discuss pros and cons of the formats. Try <code>recode</code>
to change from one character encoding to another.
</li>
<li>
Using the Python <code>csv</code> package, read a file in the default csv
format and output it in tsv format.
</li>
<li>
Define separate <code>grep -E</code> regular expressions
matching lines with
<ol>
<li>Scandinavian email address.
</li>
<li>CPR numbers.
</li>
<li>phone numbers written as 2 groups of 4 digits or 4 groups of 2 digits;
groups separated by one space.
</li>
<li>dates in the Danish format 1/1 1970.
</li>
</ol>
In all of these problems, we are interested in the <i>format</i>. Thus,
you do not have to worry about exactly which characters are legal in
email addresses, if months have 30 or 31 days, or
whether CPR numbers are legal according to checksums rules etc.
</li>
<li>Using <code>/usr/share/dict/words</code>
<!--(or <a href="https://users.cs.duke.edu/~ola/ap/linuxwords">similar</a>),-->
(or <a href="https://gist.github.com/WChargin/8927565">similar</a>),
define separate
<code>grep -E</code> regular expressions matching lines (words, since
there is only one word per line in that file) with
<ol>
<li>consecutive repetition of at least three characters.
</li>
<li>a consecutive repetition of the same sequence of four characters.
</li>
<li>a repetition of total length 4 <i>and</i> a palindrome of total length 4.
</li>
<li>words without vowels (a, e, i, o, u, y); use an option.
</li>
</ol>
</li>
<li>
Define separate <code>grep -E</code> regular
expressions matching lines with
<ol>
<li>an opening and closing html headline tag, e.g.,
<code>&lt;h2&gt;My Headline&lt;/h2&gt;</code>; use an option to make it
case insensitive, then use an option to print the line number for every match.
You may require that headlines are on a line by themselves (and of course
not nested).
</li>
<li>numbers in the range 1000 through 9999.
</li>
<li>numbers in the range 100 through 9999.
</li>
</ol>
</li>
<li>
Using <code>ls -l | grep -E REGULAR_EXPRESSION</code>,
list all files in some directory that
<ol>
<li>others can read or write (it is the 8th and 9th characters that are
relevant).
</li>
<li>were created in November and are pdf files. 
</li>
</ol>
</li>
</ol>

<p>
&nbsp;
<p>
<hr>
<p>    
<font size="2px">
<div style="font-variant: small-caps;">
&nbsp;&nbsp;
<a href="https://www.sdu.dk/en/om_sdu/om_dette_websted/databeskyttelse">Data protection at SDU</a>
&#9642;
<a href="https://www.sdu.dk/da/om_sdu/om_dette_websted/databeskyttelse">Databeskyttelse på SDU</a>
</div>
</font>
<p>

</div>
</div>
</body>
</html>
