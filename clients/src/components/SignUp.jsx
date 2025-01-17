import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'; // Import useHistory hook
import { signUp } from './api';

const SignUp = () => {
    const [userData, setUserData] = useState({
        name: '',
        email: '',
        phone: '',
        role: '',
        id_no: ''
    });

    const navigate = useNavigate(); // Initialize useNavigate hook

    const handleChange = (e) => {
        setUserData({ ...userData, [e.target.name]: e.target.value });
    };
    const [error, setError] = useState('');
    const [successMessage, setSuccessMessage] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await signUp(userData);
            console.log(response.data);
            setSuccessMessage('User signed up successfully!');
            // Redirect to the desired route after successful signup
            navigate('/applicants'); // Redirect to the applicants route
        } catch (error) {
            console.error(error);
            setError('Failed to sign up. Please try again.');
            setSuccessMessage('');
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" name="name" value={userData.name} onChange={handleChange} placeholder="Name" required />
            <input type="email" name="email" value={userData.email} onChange={handleChange} placeholder="Email" required />
            <input type="tel" name="phone" value={userData.phone} onChange={handleChange} placeholder="Phone" required />
            <input type="text" name="role" value={userData.role} onChange={handleChange} placeholder="Role" required />
            <input type="number" name="id_no" value={userData.id_no} onChange={handleChange} placeholder="ID Number" required />
            {error && <p className="error">{error}</p>}
            {successMessage && <p className="success">{successMessage}</p>}
            <button type="submit">Sign Up</button>
        </form>
    );
};

export default SignUp;
