import React from 'react'

export const Blog = () => {

    const connectionExample = () => {
        const apiUrl = 'http://127.0.0.1:8000/api/'
        try {
            fetch(apiUrl)
                .then((response) => response.json())
                .then((data) => console.log(data))
        } catch (error) {
            console.log(error)
        }
    }

    connectionExample()

    return (
        <div>
            <h1>Hola Mundo</h1>
        </div>
    )
}
