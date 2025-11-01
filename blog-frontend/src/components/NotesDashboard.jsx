import { useEffect, useState } from 'react';
import API from '../services/api';

export default function NotesDashboard() {
  const [notes, setNotes] = useState([]);
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');

  const fetchNotes = () => {
    API.get('notes/')
      .then(res => {
        console.log('Notes data:', res.data); 
        setNotes(res.data.results || []);
      })
      .catch(err => console.error('Notes error:', err));
  };

  useEffect(() => {
    fetchNotes();
  }, []);

  const createNote = async () => {
    await API.post('notes/', { title, content });
    setTitle('');
    setContent('');
    fetchNotes();
  };

  const deleteNote = async (id) => {
    await API.delete(`notes/${id}/`);
    fetchNotes();
  };

  return (
    <div>
      <h2 className="text-4xl font-bold mb-10 text-gray-800 text-center">My Private Notes</h2>
  
      <div className="bg-white p-8 rounded-2xl shadow-xl mb-10">
        <input
          placeholder="Title"
          value={title}
          onChange={e => setTitle(e.target.value)}
          className="w-full p-4 mb-4 text-lg border-2 border-gray-200 rounded-xl focus:outline-none focus:border-indigo-500 focus:ring-4 focus:ring-indigo-100 transition"
        />
        <textarea
          placeholder="Content"
          value={content}
          onChange={e => setContent(e.target.value)}
          className="w-full p-4 mb-6 text-lg border-2 border-gray-200 rounded-xl h-48 resize-none focus:outline-none focus:border-indigo-500 focus:ring-4 focus:ring-indigo-100 transition"
        />
        <button
          onClick={createNote}
          className="w-full sm:w-auto bg-gradient-to-r from-green-500 to-emerald-600 text-white px-10 py-4 rounded-xl font-bold text-lg hover:shadow-2xl transition transform hover:scale-105"
        >
          Save Note
        </button>
      </div>
  
      <div className="space-y-6">
        {notes.map(note => (
          <div key={note.id} className="bg-white p-6 rounded-2xl shadow-md hover:shadow-xl transition-all duration-300 flex justify-between items-start gap-4">
            <div className="flex-1">
              <h4 className="text-xl font-bold text-gray-800">{note.title}</h4>
              <p className="text-gray-600 mt-2">{note.content}</p>
              <small className="text-gray-400">{new Date(note.last_update).toLocaleString()}</small>
            </div>
            <button
              onClick={() => deleteNote(note.id)}
              className="bg-red-500 text-white px-4 py-2 rounded-lg hover:bg-red-600 transition font-medium"
            >
              Delete
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}