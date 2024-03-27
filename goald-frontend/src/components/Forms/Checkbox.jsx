import React from 'react'

export default function Checkbox({description}) {
    return (
      <div className="checkbox">
          <input type="checkbox" id='checkbox-id' className='checkbox__input'/>
          <span className='checkbox__button'></span>
          <label for="checkbox-id" className='checkbox__label'>{description}</label>
      </div>
    )
  }

