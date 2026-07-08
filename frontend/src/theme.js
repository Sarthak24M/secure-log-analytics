import { createTheme } from "@mui/material";

const theme = createTheme({
    palette: {
        mode: "dark",
        primary: {
            main: "#00bcd4",      // cyan accent
        },
        secondary: {
            main: "#7c4dff",      // purple for variety
        },
        error: {
            main: "#f44336",
        },
        warning: {
            main: "#ff9800",
        },
        background: {
            default: "#0a0e1a",   // deep navy
            paper: "#111827",     // slightly lighter for cards
        },
        text: {
            primary: "#e2e8f0",
            secondary: "#94a3b8",
        },
    },
    typography: {
        fontFamily: "'Inter', 'Roboto', sans-serif",
        h5: {
            fontWeight: 700,
            letterSpacing: "0.5px",
        },
        h6: {
            fontWeight: 600,
        },
        body2: {
            color: "#94a3b8",
        },
    },
    shape: {
        borderRadius: 12,
    },
    components: {
        MuiAppBar: {
            styleOverrides: {
                root: {
                    backgroundColor: "#0d1117",
                    borderBottom: "1px solid #1e293b",
                    boxShadow: "none",
                },
            },
        },
        MuiCard: {
            styleOverrides: {
                root: {
                    backgroundColor: "#111827",
                    border: "1px solid #1e293b",
                    boxShadow: "0 4px 24px rgba(0,0,0,0.4)",
                    transition: "transform 0.15s ease, box-shadow 0.15s ease",
                    "&:hover": {
                        boxShadow: "0 6px 32px rgba(0,188,212,0.15)",
                    },
                },
            },
        },
        MuiTableHead: {
            styleOverrides: {
                root: {
                    "& .MuiTableCell-root": {
                        backgroundColor: "#0d1117",
                        color: "#00bcd4",
                        fontWeight: 600,
                        fontSize: "0.75rem",
                        textTransform: "uppercase",
                        letterSpacing: "0.08em",
                        borderBottom: "1px solid #1e293b",
                    },
                },
            },
        },
        MuiTableBody: {
            styleOverrides: {
                root: {
                    "& .MuiTableRow-root": {
                        "&:hover": {
                            backgroundColor: "#1e293b",
                        },
                        "& .MuiTableCell-root": {
                            borderBottom: "1px solid #1a2234",
                            color: "#cbd5e1",
                            fontSize: "0.82rem",
                        },
                    },
                },
            },
        },
        MuiDialog: {
            styleOverrides: {
                paper: {
                    backgroundColor: "#111827",
                    border: "1px solid #1e293b",
                    borderRadius: 16,
                },
            },
        },
        MuiChip: {
            styleOverrides: {
                root: {
                    fontWeight: 600,
                    fontSize: "0.7rem",
                },
            },
        },
    },
});

export default theme;