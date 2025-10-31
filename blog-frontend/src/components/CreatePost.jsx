import { useState } from 'react';
import API from '../services/api';

export default function CreatePost() {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');

  const handleSubmit = async () => {
    await API.post('posts/', { title, content });
    alert('Post created!');
  };

  return (
    <div>
      <input placeholder="Title" onChange={e => setTitle(e.target.value)} />
      <textarea placeholder="Content" onChange={e => setContent(e.target.value)} />
      <button onClick={handleSubmit}>Post</button>
    </div>
  );
}