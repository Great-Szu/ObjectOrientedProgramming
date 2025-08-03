from hashlib import file_digest


class Song:
    """Class to represent a song
    
    Attributes:
        title (str): The title of the song
        duration (int): The duration of the song in seconds. May be zero
    """

    def __init__(self, name, duration=0):

        self.name = name
        self.duration = duration

    def get_title(self):
        return self.name


class Album:
    """ Class to represent an Album, using it's track list

    Attributes:
        name (str): The name of the album.
        year (int): The year the album was released.
        artist (Artist): The artist responsible for the album. If not specified,
        the artist will default to an artist with the name "Various Artists"
        tracks (List[Song]: A list of the song on the album.

    Methods:
        add_song: Used to add a new song to the album's track list.
    """
    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist
        self.tracks = []


    def add_song(self, song, position=None):
        """Adds a song to the track list

        Args:
            song (Song): The title of a song to add.
            position (Optional[int]): If specified, the song will be added to that position
            in the track list - inserting it between other songs if necessary.
            Otherwise, the song will be added to the end of the list.
        """
        song_found = find_object(song, self.tracks)
        if song_found is None:
            song_found = Song(song, self.artist)
            if position is None:
                self.tracks.append(song_found)
            else:
                self.tracks.insert(position, song)



class Artist:
    """ Basic class to store artist details.
    Attributes:
        name (str): The name of the artist.
        albums (List[Album]): A list of the albums by this artist.
        The list includes only those albums in this collection, it is
        not an exhaustive lists of the artist's published albums.

    Methods:
        add_album: Use to add a new album to the artist's albums list
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """ Add a new album to the list.

        Args:
            album (Album): Album object to add to the list.
        """
        self.albums.append(album)



def find_object(field, object_list):
    """Check 'object_list' to see if on object with a 'name' attribute equal to 'field' exists, return it if so"""
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():

    artist_list = []

    with open("files/albums.txt", "r") as albums:
        for line in albums:
            # data row should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            new_artist = find_object(artist_field, artist_list)

            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)

            new_album = find_object(album_field, new_artist.albums)
            if new_album is None:
                new_album = Album(album_field, year_field)
                new_artist.albums.append(new_album)

            new_song = find_object(song_field, new_album.tracks)
            if new_song is None:
                new_song = Song(song_field)
                new_album.tracks.append(new_song)

    return artist_list


def create_checkfile(artist_list):
    """ Create a check file from the object data for comparison with the original file"""
    with open("files/checkfile.txt", 'w') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.name}".format(new_artist, new_album, new_song),
                          file=checkfile)


if __name__ == '__main__':
    artists = load_data()
    print("There are {} artists".format(len(artists)))
    for album in artists[2].albums:
        for song in album.tracks:
            print(album.name, album.year, song.name)
