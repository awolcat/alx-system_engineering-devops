Shell basics: Scripts and their functions

0-current_working_directory prints the absolute path name of the current working directory.

1-listit displays the contents list of your current directory.

2-bring_me_home changes the working directory to the user’s home directory.

3-listfiles displays current directory contents in a long format

4-listmorefiles displays current directory contents, including hidden files (starting with .). Use the long format.

5-listfilesdigitonly displays current directory contents including hidden files in long format and with user and group IDs displayed numerically

6-firstdirectory creates a directory named my_first_directory in the /tmp/ directory.

7-movethatfile Moves the file betty from /tmp/ to /tmp/my_first_directory

8-firstdelete deletes the file betty from /tmp/my_first_directory/

9-firstdirdeletion deletes the directory my_first_directory that is in the /tmp  directory.

10-back changes the working directory to the previous one.

11-lists lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.

12-file_type prints the type of the file named iamafile.

13-symbolic_link creates a symbolic link to /bin/ls, named __ls__ in the current working directory

14-copy_html copies all the HTML files from the current working directory to the parent of the working directory, but only copies files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.
