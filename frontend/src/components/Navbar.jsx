import { AppBar, Toolbar, Typography } from "@mui/material";

function Navbar() {
    return (
        <AppBar position="static">
            <Toolbar>
                <Typography variant="h5">
                    Secure Log Analytics
                </Typography>
            </Toolbar>
        </AppBar>
    );
}

export default Navbar;