import { AppBar, Toolbar, Typography, Box } from "@mui/material";
import ShieldIcon from "@mui/icons-material/Shield";

function Navbar() {
    return (
        <AppBar position="static">
            <Toolbar sx={{ px: 3 }}>
                <Box sx={{ display: "flex", alignItems: "center", gap: 1.5 }}>
                    <ShieldIcon sx={{ color: "primary.main", fontSize: 28 }} />
                    <Typography variant="h5" sx={{ color: "text.primary" }}>
                        Secure Log Analytics
                    </Typography>
                </Box>
            </Toolbar>
        </AppBar>
    );
}

export default Navbar;