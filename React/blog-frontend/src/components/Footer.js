import React, { Fragment } from 'react'
import Container from '@material-ui/core/Container'
import Typography from '@material-ui/core/Typography'
import Grid from '@material-ui/core/Grid'
import Link from '@material-ui/core/Link'
import Box from '@material-ui/core/Box'
import { makeStyles } from '@material-ui/core/styles'

const useStyles = makeStyles((theme) => ({
    footer: {
        borderTop: `1px solid ${theme.palette.divider}`,
        marginTop: theme.spacing(8),
        paddingTop: theme.spacing(3),
        paddingBottom: theme.spacing(3),
        [theme.breakpoints.up('sm')]: {
            paddingTop: theme.spacing(3),
            paddingBottom: theme.spacing(6),
        },
    },
}))

const Copyright = () => {

    return (
        <Typography variant='body2' color='textSecondary' align='center'>
            {'Copyright © '}
            <Link color='inherit' href='#'>
                DjangoApiBlog
            </Link>
            {' '}{ new Date().getFullYear() }{'.'}
        </Typography>
    )
}

const footerData = [
    {
        title: 'Company',
        description: ['Team', 'History', 'Contact Us', 'Locations']
    },
    {
        title: 'Features',
        description: [
            'Cool stuff',
            'Random feature',
            'Team feature',
            'Developer stuff',
            'Another one',
        ]
    },
    {
        title: 'Resources',
        description: [
            'Resource',
            'Resource name',
            'Another resource',
            'Final resource',
        ],
    },
    {
        title: 'Legal',
        description: ['Privacy policy', 'Terms of use'],
    },
]

export const Footer = () => {

    const classes = useStyles()

    return (
        <Fragment>
            <Container maxWidth='md' component='footer' className={classes.footer}>
                <Grid container spacing={4} justify='space-evenly'>
                    {
                        footerData.map((data) => (
                            <Grid item xs={6} sm={3} key={data.title}>
                                <Typography variant='h6' color='textSecondary' gutterBottom>
                                    {data.title}
                                </Typography>
                                <ul>
                                    {
                                        data.description.map((item) => (
                                            <li key={item}>
                                                <Link href='#' variant='subtitle2' color='textSecondary'>
                                                    {item}
                                                </Link>
                                            </li>
                                        ))
                                    }
                                </ul>
                            </Grid>
                        ))
                    }
                </Grid>
                <Box marginTop={5}>
                    <Copyright />
                </Box>
            </Container>
        </Fragment>
    )
}
