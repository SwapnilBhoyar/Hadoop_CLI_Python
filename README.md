# Hadoop_CLI_Python

-mkdir : hadoop fs –mkdir /path/directory_name
Create new directory

-ls :  hadoop fs -ls /path
Using the ls command, we can check for the directories in HDFS.

-put : hadoop fs -put <localsrc> <dest>
copies files or directory from the local filesystem to the destination in the Hadoop filesystem.

-get : hadoop fs -get <src> <localdest>
copies the file or directory from the Hadoop file system to the local file system.
-copyToLocal : hadoop fs -copyToLocal <hdfs source> <localdst>
copies the file from HDFS to the local file system.
-cat : hadoop fs –cat /path_to_file_in_hdfs
reads the file in HDFS and displays the content of the file on console or stdout.
-mv : hadoop fs -mv <src> <dest>
moves the files or directories from the source to a destination within HDFS.
-cp : hadoop fs -cp <src> <dest>
copies a file from one directory to another directory within the HDFS.
-rm -r : hadoop fs -rm -r /path
Delete the files
