import { useEffect, useState } from "react";

const VideoStream = () => {
  const [streamUrl, setStreamUrl] = useState("");

  useEffect(() => {
    const serverUrl = "http://localhost:5000/video_feed"; // Flask server ka URL
    setStreamUrl(serverUrl);

    return () => {
      setStreamUrl(""); // Cleanup on unmount
    };
  }, []);

  return (
    <div className="flex justify-center items-center h-screen bg-gray-900">
      <div className="p-4 bg-gray-800 rounded-lg shadow-lg">
        <h2 className="text-white text-xl mb-4">Live Camera Stream</h2>
        {streamUrl ? (
          <img src={streamUrl} alt="Live Stream" className="w-full h-auto rounded-lg border border-gray-700" />
        ) : (
          <p className="text-white">Loading stream...</p>
        )}
      </div>
    </div>
  );
};

export default VideoStream;
