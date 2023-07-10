def cataloger(src):
    """Distribute files in the src folder into a corresponding sub-folders, 
    according to their file-type.

    Each catalogue, is a subfolder made by a filename extension

    Examples:
     /data/notes1.txt => /data/txt/notes1.txt
     /data/notes2.txt => /data/txt/notes2.txt
     /data/picture1.png => /data/png/picture1.png
     /data/track1.mp3 => /data/mp3/track1.mp3
    
    Args:
        src (string): source folder
    """
