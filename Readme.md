#  AI Notetaker

1. 1st api call to add note with the note number -  if note exists return exists message else craete and add

2. 2nd call to fetch all the existing notes

3. 3rd call to fetch a single note with the note number

api{note: str,note_no:optional[int]}:
     save notes.txt

api fetchnotes {}:
    return all notes

api fetchnote{note_no}:
return note


step 2:
signup api