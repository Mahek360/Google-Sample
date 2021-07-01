"""A video player class."""
import random
from .video_library import VideoLibrary
is_playing=False
old_video=None
now_playing=None
is_paused=False


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")
 
    def show_all_videos(self):
        """Returns all videos."""
        
        print("Here's a list of all available videos:")
        temp_list = []
        videos = self._video_library.get_all_videos()
        for vid in videos:
            #tags in required format
            tags ="["
            for tag in vid.tags:
                tags = tags + tag + " "
            tags = tags + "]"

            if tags != "[]":
                tags = tags[0:len(tags)-2] + "]"
            
            temp_list += [f"{vid.title} ({vid.video_id}) {tags}"]

        #sorts and displays the sorted list
        sorted_list = sorted(temp_list)
        for x in sorted_list:
            print(x)

    def play_video(self, video_id):
        global is_playing
        global old_video
        global is_paused

        global now_playing


        
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        play_videos = self._video_library.get_video(video_id)
        
        if not play_videos:
            print(f"Cannot play video: Video does not exist")
        else: 
            if is_playing == True:
                #print(f"Stopping video: {old_video}")
                now_playing=print(f"Playing video: {play_videos.title}")
                is_paused=False
                old_video=play_videos.title


            else:
                now_playing=print(f"Playing video: {play_videos.title}")
                is_playing = True

                is_paused=False
                old_video=play_videos.title
        
        
    def stop_video(self):
        global now_playing
        global is_playing
        global old_video


        """Stops the current video."""       
        if is_playing:
            print(f"Stopping video: {now_playing.title}")#doesn't recognise title?
            is_playing=False
            old_video=None
          

        else:
            if not is_playing:
                print(f"Cannot play video: Video does not exist")
                old_video=None
        

    def play_random_video(self):
        global is_playing
        global is_paused
        global old_video
        global now_playing
        """Plays a random video from the video library."""
        now_playing = random.choice(self._video_library.get_all_videos())

        if is_playing:
            print(f"Stopping video: {old_video}")
            print(f"Playing video: {now_playing.title}")
            is_playing=True
            is_paused=False
        else:
            print(f"Playing videos: {now_playing.title}")
            is_playing=True
            is_paused=False
        old_video=now_playing.title
       
    def pause_video(self):
        """Pauses the current video."""
        global is_paused
        global now_playing
        global is_playing
        
        if (is_paused):
            print("Video already paused: "+now_playing.title)
        elif(not(is_playing)):
            print("Cannot pause video: No video is currently playing")
        else:
            is_paused = True
            print("Pausing video: " + now_playing.title)

       

    def continue_video(self):
        """Resumes playing the current video."""
        global now_playing
        global is_paused
        
        
        if(not(now_playing)):
            print("Cannot continue video: No video is currently playing")
        elif (is_paused):
            print("Continuing video: "+now_playing.title)
            is_paused = False
        else:
            print("Cannot continue video: Video is not paused")

    def show_playing(self):
        """Displays video currently playing."""
        
        play_videos= self._video_library.get_all_videos()
        l=[]
        name=[]

        for v in play_videos:
            tags=""
            for tag in v.tags:
                tags+=tag+""
            if tags!=[]:

                tags=tags[0:len(tags)-1]

            l +=[f"{v.title} ({v.video_id}) [{tags}]"]

        for v in play_videos:
            name+=[f"{v.title}"]
        if now_playing =="":
            print("No video is currently playing")
        elif is_paused ==False:
            v=l[name.index(self.current)]

            print(f"Currently playing: {v}")
        elif is_paused ==True:
            v=l[name.index(self.current)]
            print(f"Currently playing: {v} - PAUSED")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
