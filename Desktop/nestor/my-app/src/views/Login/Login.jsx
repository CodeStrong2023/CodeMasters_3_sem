import React, { useState } from 'react';

const LoginView = () => {
  const [formData, setFormData] = useState({
    email: '',
    password: '',
  });

  const [errors, setErrors] = useState({
    email: '',
    password: '',
  });

  const validateEmail = (email) => {
    // Expresión regular para validar un correo electrónico
    const emailRegex = /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/;
    return emailRegex.test(email);
  };

  const validatePassword = (password) => {
    // Expresión regular para validar la contraseña (al menos 6 caracteres y letras y números)
    const passwordRegex = /^(?=.[A-Za-z])(?=.\d)[A-Za-z\d]{6,}$/;
    return passwordRegex.test(password);
  };

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormData({
      ...formData,
      [name]: value,
    });

    // Validar los campos mientras el usuario escribe
    if (name === 'email') {
      if (!validateEmail(value)) {
        setErrors({
          ...errors,
          email: 'Correo electrónico inválido',
        });
      } else {
        setErrors({
          ...errors,
          email: '',
        });
      }
    } else if (name === 'password') {
      if (!validatePassword(value)) {
        setErrors({
          ...errors,
          password: 'La contraseña debe contener al menos 6 caracteres, incluyendo letras y números',
        });
      } else {
        setErrors({
          ...errors,
          password: '',
        });
      }
    }
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    // Verificar si el correo y la contraseña son válidos
    if (validateEmail(formData.email) && validatePassword(formData.password)) {
      // Aquí puedes agregar lógica para iniciar sesión
      alert('Inicio de sesión exitoso');
    } else {
      alert('Correo o contraseña no válidos');
    }
  };

  return (
    <div>
      <h2>Iniciar Sesión</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Correo Electrónico:</label>
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleInputChange}
          />
          <p className="error">{errors.email}</p>
        </div>
        <div>
          <label>Contraseña:</label>
          <input
            type="password"
            name="password"
            value={formData.password}
            onChange={handleInputChange}
          />
          <p className="error">{errors.password}</p>
        </div>
        <button type="submit" disabled={!!errors.email || !!errors.password}>
          Iniciar Sesión
        </button>
      </form>
    </div>
  );
};

export default LoginView;