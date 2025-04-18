import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import ChatPage from './components/ChatPage';
import Login from './components/Login';
import Register from './components/Register';

function App() {
  return (
      <Router>
      <Routes>
        <Route
          path="/register"
          element={<Register registerEndpoint="http://localhost:8000/user/register/" />}
        ></Route>
        <Route
          path="/login"
          element={<Login loginEndpoint="http://localhost:8000/user/login/" />}
        ></Route>
        <Route path="/message" element={<ChatPage />}></Route>
        <Route path="/message/:currentSelectedChatRoom" element={<ChatPage />}></Route>
      </Routes>
    </Router>

  );
}

export default App;
