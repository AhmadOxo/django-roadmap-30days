// src/components/UserProfile.jsx
import { useEffect, useState } from 'react';
import API from '../services/api';

export default function UserProfile() {
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    const username = localStorage.getItem('username');
    if (!username) {
      console.log('No username in localStorage');
      return;
    }

    API.get(`profiles/${username}/`)
      .then(res => {
        console.log('Profile loaded:', res.data);
        setProfile(res.data);
      })
      .catch(err => {
        console.error('Profile load failed:', err.response?.data);
      });
  }, []);

  if (!profile) return <p>Loading profile...</p>;

  return (
    <div className="w-full max-w-5xl mx-auto">
      <div className="bg-white rounded-3xl shadow-2xl overflow-hidden">
        <div className="h-40 bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500"></div>
  
        <div className="relative px-8 pb-12">
          <div className="absolute -top-20 left-8">
            <div className="w-40 h-40 rounded-full border-8 border-white shadow-2xl overflow-hidden bg-gray-100">
              {profile.avatar ? (
                <img src={profile.avatar} alt="Avatar" className="w-full h-full object-cover" />
              ) : (
                <div className="flex items-center justify-center w-full h-full bg-gradient-to-br from-indigo-400 to-purple-600 text-white text-5xl font-bold">
                  {profile.username.charAt(0).toUpperCase()}
                </div>
              )}
            </div>
          </div>
  
          <div className="pt-24 text-center sm:text-left">
            <h2 className="text-4xl font-bold text-gray-800">{profile.username}</h2>
            <p className="text-gray-600 mt-3 text-lg">{profile.bio || 'No bio yet. Add one!'}</p>
  
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-6 mt-10">
              <div className="bg-gradient-to-br from-indigo-50 to-blue-50 rounded-2xl p-6 text-center">
                <p className="text-4xl font-bold text-indigo-600">{profile.post_count}</p>
                <p className="text-gray-600 font-medium">Posts</p>
              </div>
              <div className="bg-gradient-to-br from-purple-50 to-pink-50 rounded-2xl p-6 text-center">
                <p className="text-4xl font-bold text-purple-600">{profile.note_count || 0}</p>
                <p className="text-gray-600 font-medium">Notes</p>
              </div>
              <div className="bg-gradient-to-br from-pink-50 to-red-50 rounded-2xl p-6 text-center">
                <p className="text-lg font-bold text-pink-600">
                  {new Date(profile.date_joined).toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })}
                </p>
                <p className="text-gray-600 font-medium">Member Since</p>
              </div>
            </div>
  
            <div className="mt-10 text-center">
              <button className="bg-gradient-to-r from-indigo-600 to-purple-600 text-white px-12 py-4 rounded-full font-bold text-lg hover:shadow-2xl transition transform hover:scale-105">
                Edit Profile
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}