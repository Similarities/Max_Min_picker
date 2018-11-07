# Max_Min_picker
full numeric scan, works for modulations on a nonlinear background

=======================================================
Max _ Min picker is used to collect the maximum and minimum out of x,y dataset. This is usefull tool 
for modulations in a dataset. The simplest way to find max min often relies on absolute values, 
meaning a some kind constant background on which the modulation appears and can be easily discriminated 
by a threshold value. For a nonlinear relation of the background (see example) the modulation is on 
top of a complex function - which might be not be so easy to linearized by fit. 
This approach tries to find max - min values via a modified next neighbor approach. The scan compares
next neighbors for change of sign in the slope. This of course includes three points that has to be
compared. To get the modulation periods that are T>3 px, here entries of the dataset with no 
change in the slope are deleted.
