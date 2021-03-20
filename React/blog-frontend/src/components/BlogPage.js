import React, { useEffect, useState } from 'react'

import Typography from '@material-ui/core/Typography'
import Container from '@material-ui/core/Container'
import { makeStyles } from '@material-ui/core'

import { Blog } from './Blog'

const useStyles = makeStyles((theme) => ({
    blogPageContent: {
        padding: theme.spacing(8, 0, 6),
    },
}))

export const BlogPage = () => {
    
    const classes = useStyles()

    const [blogs, setBlogs] = useState({
        loading: false,
        blogs: null
    })

    useEffect(() => {
        setBlogs({
            loading: true
        })
        const apiUrl = 'http://127.0.0.1:8000/api/'
        try {
            fetch(apiUrl)
                .then((data) => data.json())
                .then((blogs) => {
                    setBlogs({
                        loading: false,
                        blogs: blogs
                    })
                })
        } catch (error) {
            console.log(error)
        }
    }, [])

    return (
        <div>
            <Container maxWidth="sm" component="main" className={classes.blogPageContent}>
                <Typography variant="h3" align="center" color="textPrimary" gutterBottom>
                    Django API Blogs
                </Typography>
                <Typography variant="h5" align="center" color="textSecondary" component="p">
                    Django and React project using django REST framework library
                </Typography>
            </Container>
            {
                blogs.loading
                ? <p style={{ fontSize: '25px' }}>Loading</p>
                : <Blog blogs={blogs.blogs} />
            }
        </div>
    )
}
