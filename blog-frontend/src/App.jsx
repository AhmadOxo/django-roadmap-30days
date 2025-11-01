import { Routes, Route, Navigate } from 'react-router-dom';
import Login from './components/Login';
import PostList from './components/PostList';
import CreatePost from './components/CreatePost';
import NotesDashboard from './components/NotesDashboard';
import UserProfile from './components/UserProfile';


function App() {
  const token = localStorage.getItem('access_token');

  return (
    
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 w-full">
      {/* HEADER */}
      <header className="bg-white shadow-sm border-b w-full">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex justify-between items-center">
          <h1 className="text-3xl font-bold text-indigo-700">MyBlog</h1>
          {token && (
            <nav className="flex gap-6 items-center">
              <a href="/posts" className="text-indigo-600 hover:text-indigo-800 font-medium text-lg">Posts</a>
              <a href="/create" className="text-indigo-600 hover:text-indigo-800 font-medium text-lg">Create</a>
              <a href="/notes" className="text-indigo-600 hover:text-indigo-800 font-medium text-lg">Notes</a>
              <a href="/profile" className="text-indigo-600 hover:text-indigo-800 font-medium text-lg">Profile</a>
              <button
                onClick={() => { localStorage.clear(); window.location.href = '/' }}
                className="bg-red-500 text-white px-5 py-2 rounded-lg hover:bg-red-600 transition font-medium"
              >
                Logout
              </button>
            </nav>
          )}
        </div>
      </header>

      {/* MAIN CONTENT — CONSISTENT WIDTH */}
      <main className="py-10">
        <Routes>
          <Route path="/" element={!token ? <Login /> : <Navigate to="/posts" />} />
          <Route path="/posts" element={token ? <PostList /> : <Navigate to="/" />} />
          <Route path="/create" element={token ? <CreatePost /> : <Navigate to="/" />} />
          <Route path="/notes" element={token ? <NotesDashboard /> : <Navigate to="/" />} />
          <Route path="/profile" element={token ? <UserProfile /> : <Navigate to="/" />} />
        </Routes>
      </main>
    </div>
  
  );
}
export default App;