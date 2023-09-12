# Powells_method
Window app for searching minimum of nonlinear functions using *Powells Method* with visualization in Matplotlib. This project is renewed version of project made for classes of **Theory and Methods of Optymalization** at <b>*WUST*</b>.

# Algorithms
Project uses [Powell Methods](https://en.wikipedia.org/wiki/Powell%27s_method) to find minimum of function with 2-5 variables. In addition, it is used [Golden Section Search](https://en.wikipedia.org/wiki/Golden-section_search) to find minimum inside an interval. 

In purpose to parse function from **string** there were used **eval()** function with *white list*.


# Software
App was tested on **Windows10, Windows11 and Ubuntu20.04** with **Python3.8 and Python3.9**.

GUI was written using **Tkinter** library.  


# Dependecies
Libraries that may required installing:
<ul>
<li>    matplotlib 3.1.2
<li>    numpy 1.23.5
<li>    tk 0.1.0
</ul>




# Documentation

Documentation can be generate using Doxygen or Doxywizard with one of following command:
<ul>
<li>    <i>doxygen Doxyfile</i>
<li>    <i>doxywizard Doxyfile</i>  -- and then <i>run</i> button.
</ul>