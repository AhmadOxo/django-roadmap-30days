import { useEffect, useState } from 'react';
import API from '../services/api';

export default function PostList() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    API.get('posts/').then(res => setPosts(res.data.results));
  }, []);

  return (
    <div>
      <h2 className="text-4xl font-bold mb-10 text-gray-800 text-center">Latest Posts</h2>
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
        {posts.map(post => (
          <div key={post.id} className="bg-white p-6 rounded-2xl shadow-lg hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2 h-full flex flex-col">
            <h3 className="text-xl font-bold text-indigo-700 mb-3 flex-grow">{post.title}</h3>
            <p className="text-gray-600 mb-4 line-clamp-3 flex-grow">{post.content}</p>
            <div className="mt-auto">
              <p className="text-sm text-gray-500">by <strong>{post.author}</strong></p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}