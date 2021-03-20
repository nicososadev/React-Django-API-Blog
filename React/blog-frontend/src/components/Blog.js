import React, { Fragment } from 'react'

import Typography from '@material-ui/core/Typography'
import Container from '@material-ui/core/Container'
import Grid from '@material-ui/core/Grid'
import Card from '@material-ui/core/Card'
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent'
import CardMedia from '@material-ui/core/CardMedia'
import Button from '@material-ui/core/Button';
import { makeStyles } from '@material-ui/core'

const useStyles = makeStyles((theme) => ({
    link: {
        margin: theme.spacing(1, 1.5),
    },
    cardHeader: {
        backgroundColor: 
            theme.palette.type === 'light'
                ? theme.palette.grey[200]
                : theme.palette.grey[700],
        
    },
    blogCard: {
        maxWidth: 345,
    },
    blogContent: {
        display: 'flex',
        justifyContent: 'left',
        alignItems: 'baseline',
        fontSize: '12px',
        textAlign: 'left',
        marginBottom: theme.spacing(2),
        maxHeight: theme.spacing(2)
    }
}))

export const Blog = (props) => {

    const { blogs } = props

    console.log(props)

    const classes = useStyles()

    if (!blogs || blogs.length === 0){
        return (
            <p>Can not find any blogs</p>
        )
    }

    return (
        <Fragment>
            <Container maxWidth='md' component='main'>
                <Grid container spacing={5} alignItems='flex-end'>
                    {
                        blogs.map((blog) => {
                            return (
                                <Grid item key={blog.id} xs={12} md={4}>
                                    <Card className={classes.blogCard}>
                                        <CardMedia 
                                            component='img'
                                            height="140"
                                            image='https://source.unsplash.com/random'
                                            title='Image Title'
                                        />
                                        <CardContent>
                                            <Typography 
                                                gutterBottom
                                                variant='h5'
                                                component='h2'
                                            >
                                                {blog.title}
                                            </Typography>
                                            <Typography 
                                                className={classes.blogContent}
                                                variant='body2'
                                                component='p'
                                                color='textSecondary'
                                            >
                                                {blog.content}
                                            </Typography>
                                        </CardContent>
                                        <CardActions>
                                            <Button size="small" color="primary">
                                                Learn More
                                            </Button>
                                        </CardActions>
                                    </Card>
                                </Grid>
                            )
                        })
                    }
                </Grid>
            </Container>
        </Fragment>
    )
}
