import React from 'react'

import './placeholder.scss'

export default function Placeholder({description, isPassword = false}) {
    return (
      <div className='placeholder'>
          <span className="placeholder__description">{description}</span>
          <input type={isPassword ? "password" : "text"} className="placeholder__field" required />
      </div>
    )
}