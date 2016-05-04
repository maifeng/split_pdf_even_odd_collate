Split PDF file to multiple groups
-----------------
Requires PyPDF2

This python script can be used to collate a single pdf file to multiple pdf files. One usage situation is to use it as the "anti-collate" for your scanned file. It can also be used to split a file to even-odd pages.

For example, if you would like to split a file named "all.pdf" to 3 files, each containing pages: 

```
group0.pdf: 1, 4, 7, 10...
group1.pdf: 2, 5, 8, 11...
group2.pdf: 3, 6, 9, 12...
```

You can use
```python
python split_by_group.py all.pdf 3 group
```

The three arguments are: input filename, number of files to split, output file prefix.