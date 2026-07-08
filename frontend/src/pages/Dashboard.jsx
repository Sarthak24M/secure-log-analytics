import {
    Box,
    Typography,
    CircularProgress,
    Alert,
    Dialog,
    DialogTitle,
    DialogContent,
    IconButton,
    Table,
    TableHead,
    TableBody,
    TableRow,
    TableCell,
    Chip,
    Divider,
} from "@mui/material";
import CloseIcon from "@mui/icons-material/Close";
import SecurityIcon from "@mui/icons-material/Security";
import ReportProblemIcon from "@mui/icons-material/ReportProblem";
import LockIcon from "@mui/icons-material/Lock";
import PersonIcon from "@mui/icons-material/Person";
import EventNoteIcon from "@mui/icons-material/EventNote";
import { useEffect, useState } from "react";

import Navbar from "../components/Navbar";
import SummaryCard from "../components/SummaryCard";
import { getSummary, getAnalytics, getDetections } from "../services/api";

// ── Severity chip colours ──────────────────────────────────────────────────
const severityColor = {
    HIGH: "error",
    MEDIUM: "warning",
    LOW: "success",
};

// ── Small reusable section heading ─────────────────────────────────────────
function SectionTitle({ children }) {
    return (
        <Typography
            variant="h6"
            sx={{ color: "text.primary", mb: 2, mt: 5, fontWeight: 700 }}
        >
            {children}
        </Typography>
    );
}

// ── Generic log table ──────────────────────────────────────────────────────
function LogTable({ rows }) {
    if (!rows || rows.length === 0) {
        return (
            <Typography variant="body2" sx={{ color: "text.secondary", py: 2 }}>
                No records found.
            </Typography>
        );
    }

    const columns = Object.keys(rows[0]);

    return (
        <Box sx={{ overflowX: "auto" }}>
            <Table size="small">
                <TableHead>
                    <TableRow>
                        {columns.map((col) => (
                            <TableCell key={col}>{col.replace(/_/g, " ")}</TableCell>
                        ))}
                    </TableRow>
                </TableHead>
                <TableBody>
                    {rows.map((row, i) => (
                        <TableRow key={i}>
                            {columns.map((col) => (
                                <TableCell key={col}>
                                    {col === "severity" ? (
                                        <Chip
                                            label={row[col]}
                                            color={severityColor[row[col]] || "default"}
                                            size="small"
                                        />
                                    ) : (
                                        row[col] ?? "—"
                                    )}
                                </TableCell>
                            ))}
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
        </Box>
    );
}

// ── Log detail dialog ──────────────────────────────────────────────────────
function LogDialog({ open, onClose, title, rows }) {
    return (
        <Dialog open={open} onClose={onClose} maxWidth="lg" fullWidth>
            <DialogTitle
                sx={{
                    display: "flex",
                    justifyContent: "space-between",
                    alignItems: "center",
                    pb: 1,
                }}
            >
                <Typography variant="h6" fontWeight={700}>
                    {title}
                </Typography>
                <IconButton onClick={onClose} size="small" sx={{ color: "text.secondary" }}>
                    <CloseIcon />
                </IconButton>
            </DialogTitle>
            <Divider sx={{ borderColor: "#1e293b" }} />
            <DialogContent sx={{ pt: 2 }}>
                <LogTable rows={rows} />
            </DialogContent>
        </Dialog>
    );
}

// ── Card config ────────────────────────────────────────────────────────────
// Maps each summary card to its dialog data and visual style.
// detectionKey refers to a key inside the detections API response.
const CARD_CONFIG = [
    {
        key: "total_events",
        title: "Total Events",
        icon: <EventNoteIcon />,
        accentColor: "#00bcd4",
        detectionKey: null,         // no drill-down for total
    },
    {
        key: "authentication_failures",
        title: "Failed Logins",
        icon: <LockIcon />,
        accentColor: "#f44336",
        detectionKey: "authentication_failures",
    },
    {
        key: "high_severity_alerts",
        title: "High Alerts",
        icon: <SecurityIcon />,
        accentColor: "#ff5722",
        detectionKey: "high_severity_alerts",
    },
    {
        key: "password_changes",
        title: "Password Changes",
        icon: <PersonIcon />,
        accentColor: "#ff9800",
        detectionKey: "password_changes",
    },
    {
        key: "privileged_commands",
        title: "Privileged Commands",
        icon: <ReportProblemIcon />,
        accentColor: "#7c4dff",
        detectionKey: "excessive_privileged_commands",
    },
];

// ── Dashboard ──────────────────────────────────────────────────────────────
function Dashboard() {
    const [summary, setSummary]       = useState(null);
    const [analytics, setAnalytics]   = useState(null);
    const [detections, setDetections] = useState(null);
    const [loading, setLoading]       = useState(true);
    const [error, setError]           = useState(null);
    const [dialog, setDialog]         = useState({ open: false, title: "", rows: [] });

    useEffect(() => {
        async function fetchAll() {
            try {
                const [s, a, d] = await Promise.all([
                    getSummary(),
                    getAnalytics(),
                    getDetections(),
                ]);
                setSummary(s);
                setAnalytics(a);
                setDetections(d);
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        }
        fetchAll();
    }, []);

    const openDialog = (title, rows) => setDialog({ open: true, title, rows });
    const closeDialog = () => setDialog({ open: false, title: "", rows: [] });

    // ── Loading ──────────────────────────────────────────────────────────
    if (loading) {
        return (
            <Box sx={{ minHeight: "100vh", bgcolor: "background.default" }}>
                <Navbar />
                <Box sx={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", height: "80vh", gap: 2 }}>
                    <CircularProgress color="primary" />
                    <Typography variant="body2" color="text.secondary">
                        Processing log pipeline…
                    </Typography>
                </Box>
            </Box>
        );
    }

    // ── Error ────────────────────────────────────────────────────────────
    if (error) {
        return (
            <Box sx={{ minHeight: "100vh", bgcolor: "background.default" }}>
                <Navbar />
                <Box sx={{ p: 4 }}>
                    <Alert severity="error" sx={{ maxWidth: 600 }}>
                        Failed to load dashboard data: {error}
                    </Alert>
                </Box>
            </Box>
        );
    }

    // ── Main render ──────────────────────────────────────────────────────
    return (
        <Box sx={{ minHeight: "100vh", bgcolor: "background.default" }}>
            <Navbar />

            <Box sx={{ px: { xs: 2, sm: 4 }, py: 4, maxWidth: 1400, mx: "auto" }}>

                {/* ── Summary Cards ──────────────────────────────────── */}
                <Box sx={{ display: "flex", gap: 2.5, flexWrap: "wrap", mb: 2 }}>
                    {CARD_CONFIG.map(({ key, title, icon, accentColor, detectionKey }) => (
                        <SummaryCard
                            key={key}
                            title={title}
                            value={summary[key]}
                            icon={icon}
                            accentColor={accentColor}
                            onClick={
                                detectionKey
                                    ? () => openDialog(title, detections[detectionKey])
                                    : undefined
                            }
                        />
                    ))}
                </Box>

                {/* ── Event Distribution ─────────────────────────────── */}
                <SectionTitle>Event Distribution</SectionTitle>
                <LogTable rows={analytics.event_distribution} />

                {/* ── Authentication Summary ─────────────────────────── */}
                <SectionTitle>Authentication Summary</SectionTitle>
                <LogTable rows={analytics.authentication_summary} />

                {/* ── Top Users ──────────────────────────────────────── */}
                <SectionTitle>Top Users</SectionTitle>
                <LogTable rows={analytics.top_users} />

                {/* ── Top Processes ──────────────────────────────────── */}
                <SectionTitle>Top Processes</SectionTitle>
                <LogTable rows={analytics.top_processes} />

                {/* ── Brute Force Detections ─────────────────────────── */}
                <SectionTitle>Brute Force Detections</SectionTitle>
                <LogTable rows={detections.brute_force} />

                {/* ── Root Activity ──────────────────────────────────── */}
                <SectionTitle>Root Activity</SectionTitle>
                <LogTable rows={detections.root_activity} />

            </Box>

            {/* ── Log Detail Dialog ───────────────────────────────────── */}
            <LogDialog
                open={dialog.open}
                onClose={closeDialog}
                title={dialog.title}
                rows={dialog.rows}
            />
        </Box>
    );
}

export default Dashboard;