---
toc: True
comments: false
layout: post
title: Ranking Table
description: Top 5 English Premier League Teams in 2022-2023 Season
courses: { compsci: {week: 2} }
type: hacks
---

<!-- Include DataTables CSS -->
<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.11.5/css/jquery.dataTables.css">

<!-- Include jQuery -->
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

<!-- Include DataTables JavaScript -->
<script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.js"></script>

<table id="teamTable" class="table">
    <thead>
        <tr>
            <th>Club</th>
            <th>MP</th>
            <th>W</th>
            <th>D</th>
            <th>L</th>
            <th>Market Value</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Man City</td>
            <td>38</td>
            <td>28</td>
            <td>5</td>
            <td>5</td>
            <td>€1.18bn</td>
        </tr>
        <tr>
            <td>Arsenal</td>
            <td>38</td>
            <td>26</td>
            <td>6</td>
            <td>6</td>
            <td>€1.11bn</td>
        </tr>
        <tr>
            <td>Man United</td>
            <td>38</td>
            <td>23</td>
            <td>6</td>
            <td>9</td>
            <td>€882.30m</td>
        </tr>
        <tr>
            <td>Newcastle</td>
            <td>38</td>
            <td>19</td>
            <td>14</td>
            <td>5</td>
            <td>€598.00m</td>
        </tr>
        <tr>
            <td>Liverpool</td>
            <td>38</td>
            <td>19</td>
            <td>10</td>
            <td>9</td>
            <td>€827.30m</td>
        </tr>
    </tbody>
</table>

<script>
$(document).ready(function() {
    $('#teamTable').DataTable();
});
</script>
