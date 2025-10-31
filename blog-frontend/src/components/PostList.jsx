import { useEffect, useState } from 'react';
import API from '../services/api';

export default function PostList() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    API.get('posts/').then(res => setPosts(res.data.results));
  }, []);

  return (
    <div>
      {posts.map(post => (
        <div key={post.id}>
          <h3>{post.title}</h3>
          <p>{post.content}</p>
          <small>by {post.author}</small>
        </div>
      ))}
    </div>
  );
}