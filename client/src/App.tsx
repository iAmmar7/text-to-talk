import { useRef, useState } from 'react';
import { PlayIcon } from './icons/PlayIcon';
import LoaderIcon from './icons/LoaderIcon';
import {
  API_URL,
  MAX_TEXT_LENGTH,
  MIN_TEXT_LENGTH,
  SAMPLE_TEXT,
} from './utils/constants';

const App = () => {
  const [text, setText] = useState(SAMPLE_TEXT);
  const [isSending, setIsSending] = useState(false);
  const [audioUrl, setAudioUrl] = useState<string | null>(null);
  const [cachedText, setCachedText] = useState(SAMPLE_TEXT);
  const audioRef = useRef<HTMLAudioElement | null>(null);

  const isTextValid =
    text.trim().length > MIN_TEXT_LENGTH &&
    text.trim().length < MAX_TEXT_LENGTH;

  const playAudio = () => {
    if (audioRef.current) {
      audioRef.current.play();
    }
  };

  const stopAudio = () => {
    if (audioRef.current) {
      audioRef.current.pause();
      audioRef.current.currentTime = 0;
    }
  };

  const handleSend = async () => {
    if (!isTextValid) {
      alert('Text length should be in range!');
      return;
    }

    try {
      setIsSending(true);

      // If the current text matches the cached text; play the old audio
      if (text === cachedText && audioUrl) {
        stopAudio();
        audioRef.current = new Audio(audioUrl);
        playAudio();
        return;
      }

      // Send the request to the server
      const response = await fetch(`${API_URL}/summarize-to-speech`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      // Convert response to Blob (audio buffer)
      const audioBlob = await response.blob();

      // Create a URL for the audio
      const newAudioUrl = URL.createObjectURL(audioBlob);

      // Cache the audio and text
      setAudioUrl(newAudioUrl);
      setCachedText(text);

      // Play the new audio
      audioRef.current = new Audio(newAudioUrl);
      playAudio();
    } catch (error) {
      console.error('Error:', error);
      setAudioUrl(null);
      setCachedText('');
      audioRef.current = null;
      alert('An error occurred while processing your request.');
    } finally {
      setIsSending(false);
    }
  };

  return (
    <div className='h-screen w-full flex flex-col justify-center overflow-hidden'>
      <div className='container m-auto my-6 rounded-md shadow-md max-w-2xl'>
        <div className='w-full flex flex-col p-4'>
          <h1 className='text-4xl font-bold m-auto mb-4'>Text to Talk</h1>
          <label
            htmlFor='textInput'
            className='text-base text-left mb-2 font-bold'
          >
            Enter text to summarize and convert to speech:
          </label>
          <textarea
            id='textInput'
            className='w-full p-2 rounded-md focus:outline-none focus:ring-blue-500 bg-[#242424] ring-2 ring-gray-500'
            rows={10}
            placeholder='Type your text here...'
            value={text}
            onChange={(e) => setText(e.target.value)}
          />
          <div className='flex justify-between content-center mt-4'>
            <span className='text-sm'>
              <p>
                Min length is{' '}
                <span className='font-bold'>{MIN_TEXT_LENGTH}</span>
              </p>
              <p>
                Max length is{' '}
                <span className='font-bold'>{MAX_TEXT_LENGTH}</span>
              </p>
            </span>
            <button
              className='flex items-center justify-center gap-2 px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 active:bg-blue-700 disabled:bg-gray-500 border-none'
              onClick={handleSend}
              disabled={isSending || !isTextValid}
            >
              <span className='w-5'>
                {isSending ? (
                  <LoaderIcon className='h-5 w-5' />
                ) : (
                  <PlayIcon className='h-5 w-5 mr-2' />
                )}
              </span>
              Play
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default App;
