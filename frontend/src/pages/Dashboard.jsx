import { Box } from "@mui/material";
import { useEffect, useState } from "react";

import Navbar from "../components/Navbar";
import SummaryCard from "../components/SummaryCard";
import { getSummary } from "../services/api";

function Dashboard() {
    const [summary, setSummary] = useState(null);


    useEffect(() => {

    async function fetchSummary() {

        try {

            const data = await getSummary();

            setSummary(data);

        }

        catch (error) {

            console.error(error);

        }

    }

    fetchSummary();

    }, []);

    if (!summary) {

    return <h2>Loading...</h2>;

    }




    return (

        <>

            <Navbar />

            <Box
                sx={{
                    display: "flex",
                    gap: 3,
                    padding: 4,
                    flexWrap: "wrap"
                }}
            >

                <SummaryCard
                    title="Total Events"
                    value={289}
                />

                <SummaryCard
                    title="Failed Logins"
                    value={5}
                />

                <SummaryCard
                    title="High Alerts"
                    value={5}
                />

                <SummaryCard
                    title="Password Changes"
                    value={1}
                />

                <SummaryCard
                    title="Privileged Commands"
                    value={8}
                />

            </Box>

        </>

    );
}

export default Dashboard;