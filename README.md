# Stock Market Game

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) &nbsp;
[![forthebadge](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzNzUuNjA5OTk5OTk5OTk5OTYiIGhlaWdodD0iMzUiIHZpZXdCb3g9IjAgMCAzNzUuNjA5OTk5OTk5OTk5OTYgMzUiPjxyZWN0IGNsYXNzPSJzdmdfX3JlY3QiIHg9IjAiIHk9IjAiIHdpZHRoPSIxOTQuNjc5OTk5OTk5OTk5OTgiIGhlaWdodD0iMzUiIGZpbGw9IiMzMUM0RjMiLz48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSIxOTIuNjc5OTk5OTk5OTk5OTgiIHk9IjAiIHdpZHRoPSIxODIuOTI5OTk5OTk5OTk5OTgiIGhlaWdodD0iMzUiIGZpbGw9IiMzODlBRDUiLz48cGF0aCBjbGFzcz0ic3ZnX190ZXh0IiBkPSJNMTUuMDAgMjJMMTMuNDYgMjJMMTYuNjggMTMuNDdMMTguMDEgMTMuNDdMMjEuMjQgMjJMMTkuNjkgMjJMMTguOTkgMjAuMDFMMTUuNjkgMjAuMDFMMTUuMDAgMjJaTTE3LjM0IDE1LjI4TDE2LjEwIDE4LjgyTDE4LjU4IDE4LjgyTDE3LjM0IDE1LjI4Wk0yNi42NyAyMkwyNS4xOSAyMkwyNS4xOSAxMy40N0wyNi42NyAxMy40N0wzMC40OSAxOS41NEwzMC40OSAxMy40N0wzMS45NiAxMy40N0wzMS45NiAyMkwzMC40OCAyMkwyNi42NyAxNS45NUwyNi42NyAyMlpNMzkuMTUgMjJMMzYuNzAgMjJMMzYuNzAgMTMuNDdMMzkuMjIgMTMuNDdRNDAuMzUgMTMuNDcgNDEuMjMgMTMuOTdRNDIuMTAgMTQuNDggNDIuNTggMTUuNDBRNDMuMDYgMTYuMzMgNDMuMDYgMTcuNTJMNDMuMDYgMTcuNTJMNDMuMDYgMTcuOTVRNDMuMDYgMTkuMTYgNDIuNTggMjAuMDhRNDIuMTAgMjEuMDAgNDEuMjAgMjEuNTBRNDAuMzEgMjIgMzkuMTUgMjJMMzkuMTUgMjJaTTM4LjE4IDE0LjY2TDM4LjE4IDIwLjgyTDM5LjE1IDIwLjgyUTQwLjMxIDIwLjgyIDQwLjk0IDIwLjA5UTQxLjU2IDE5LjM2IDQxLjU3IDE3Ljk5TDQxLjU3IDE3Ljk5TDQxLjU3IDE3LjUyUTQxLjU3IDE2LjEzIDQwLjk3IDE1LjQwUTQwLjM3IDE0LjY2IDM5LjIyIDE0LjY2TDM5LjIyIDE0LjY2TDM4LjE4IDE0LjY2Wk01NC45OSAyMkw1My41MCAyMkw1My41MCAxMy40N0w1NC45OSAxMy40N0w1NC45OSAxNy4wMkw1OC44MCAxNy4wMkw1OC44MCAxMy40N0w2MC4yOCAxMy40N0w2MC4yOCAyMkw1OC44MCAyMkw1OC44MCAxOC4yMUw1NC45OSAxOC4yMUw1NC45OSAyMlpNNzAuNjAgMjJMNjUuMDIgMjJMNjUuMDIgMTMuNDdMNzAuNTYgMTMuNDdMNzAuNTYgMTQuNjZMNjYuNTAgMTQuNjZMNjYuNTAgMTcuMDJMNzAuMDAgMTcuMDJMNzAuMDAgMTguMTlMNjYuNTAgMTguMTlMNjYuNTAgMjAuODJMNzAuNjAgMjAuODJMNzAuNjAgMjJaTTgwLjE1IDIyTDc0Ljc5IDIyTDc0Ljc5IDEzLjQ3TDc2LjI3IDEzLjQ3TDc2LjI3IDIwLjgyTDgwLjE1IDIwLjgyTDgwLjE1IDIyWk04Ni43MyAyMkw4NC4yNyAyMkw4NC4yNyAxMy40N0w4Ni43OSAxMy40N1E4Ny45MiAxMy40NyA4OC44MCAxMy45N1E4OS42NyAxNC40OCA5MC4xNSAxNS40MFE5MC42NCAxNi4zMyA5MC42NCAxNy41Mkw5MC42NCAxNy41Mkw5MC42NCAxNy45NVE5MC42NCAxOS4xNiA5MC4xNSAyMC4wOFE4OS42NyAyMS4wMCA4OC43NyAyMS41MFE4Ny44OCAyMiA4Ni43MyAyMkw4Ni43MyAyMlpNODUuNzUgMTQuNjZMODUuNzUgMjAuODJMODYuNzIgMjAuODJRODcuODkgMjAuODIgODguNTEgMjAuMDlRODkuMTQgMTkuMzYgODkuMTUgMTcuOTlMODkuMTUgMTcuOTlMODkuMTUgMTcuNTJRODkuMTUgMTYuMTMgODguNTQgMTUuNDBRODcuOTQgMTQuNjYgODYuNzkgMTQuNjZMODYuNzkgMTQuNjZMODUuNzUgMTQuNjZaTTEwMi43NiAxNC42NkwxMDAuMTIgMTQuNjZMMTAwLjEyIDEzLjQ3TDEwNi44OSAxMy40N0wxMDYuODkgMTQuNjZMMTA0LjIzIDE0LjY2TDEwNC4yMyAyMkwxMDIuNzYgMjJMMTAyLjc2IDE0LjY2Wk0xMTAuMzggMTguMDBMMTEwLjM4IDE4LjAwTDExMC4zOCAxNy41MlExMTAuMzggMTYuMjggMTEwLjgyIDE1LjMyUTExMS4yNiAxNC4zNyAxMTIuMDcgMTMuODZRMTEyLjg3IDEzLjM1IDExMy45MSAxMy4zNVExMTQuOTYgMTMuMzUgMTE1Ljc2IDEzLjg1UTExNi41NyAxNC4zNSAxMTcuMDEgMTUuMjlRMTE3LjQ1IDE2LjIzIDExNy40NSAxNy40OEwxMTcuNDUgMTcuNDhMMTE3LjQ1IDE3Ljk2UTExNy40NSAxOS4yMSAxMTcuMDIgMjAuMTZRMTE2LjU5IDIxLjEwIDExNS43OCAyMS42MVExMTQuOTcgMjIuMTIgMTEzLjkzIDIyLjEyTDExMy45MyAyMi4xMlExMTIuODkgMjIuMTIgMTEyLjA4IDIxLjYxUTExMS4yNyAyMS4xMCAxMTAuODIgMjAuMTdRMTEwLjM4IDE5LjIzIDExMC4zOCAxOC4wMFpNMTExLjg2IDE3LjQ2TDExMS44NiAxNy45NlExMTEuODYgMTkuMzYgMTEyLjQxIDIwLjEzUTExMi45NSAyMC45MCAxMTMuOTMgMjAuOTBMMTEzLjkzIDIwLjkwUTExNC45MSAyMC45MCAxMTUuNDQgMjAuMTVRMTE1Ljk3IDE5LjQwIDExNS45NyAxNy45NkwxMTUuOTcgMTcuOTZMMTE1Ljk3IDE3LjUxUTExNS45NyAxNi4wOSAxMTUuNDMgMTUuMzRRMTE0LjkwIDE0LjU4IDExMy45MSAxNC41OEwxMTMuOTEgMTQuNThRMTEyLjk1IDE0LjU4IDExMi40MSAxNS4zM1ExMTEuODcgMTYuMDkgMTExLjg2IDE3LjQ2TDExMS44NiAxNy40NlpNMTIxLjY3IDE4LjEzTDEyMS42NyAxOC4xM0wxMjEuNjcgMTcuNDZRMTIxLjY3IDE1LjUzIDEyMi42MCAxNC40NFExMjMuNTIgMTMuMzUgMTI1LjE4IDEzLjM1TDEyNS4xOCAxMy4zNVExMjYuNjEgMTMuMzUgMTI3LjQ0IDE0LjA1UTEyOC4yOCAxNC43NiAxMjguNDUgMTYuMDhMMTI4LjQ1IDE2LjA4TDEyNy4wMCAxNi4wOFExMjYuNzUgMTQuNTQgMTI1LjIxIDE0LjU0TDEyNS4yMSAxNC41NFExMjQuMjIgMTQuNTQgMTIzLjcwIDE1LjI2UTEyMy4xOCAxNS45OCAxMjMuMTYgMTcuMzdMMTIzLjE2IDE3LjM3TDEyMy4xNiAxOC4wMlExMjMuMTYgMTkuNDAgMTIzLjc0IDIwLjE3UTEyNC4zMyAyMC45MyAxMjUuMzYgMjAuOTNMMTI1LjM2IDIwLjkzUTEyNi41MCAyMC45MyAxMjYuOTggMjAuNDJMMTI2Ljk4IDIwLjQyTDEyNi45OCAxOC43NUwxMjUuMjIgMTguNzVMMTI1LjIyIDE3LjYyTDEyOC40NiAxNy42MkwxMjguNDYgMjAuODlRMTI3Ljk5IDIxLjUwIDEyNy4xNyAyMS44MVExMjYuMzUgMjIuMTIgMTI1LjMxIDIyLjEyTDEyNS4zMSAyMi4xMlExMjQuMjQgMjIuMTIgMTIzLjQxIDIxLjYzUTEyMi41OSAyMS4xNCAxMjIuMTQgMjAuMjRRMTIxLjY5IDE5LjMzIDEyMS42NyAxOC4xM1pNMTM4LjY1IDIyTDEzMy4wNyAyMkwxMzMuMDcgMTMuNDdMMTM4LjYxIDEzLjQ3TDEzOC42MSAxNC42NkwxMzQuNTYgMTQuNjZMMTM0LjU2IDE3LjAyTDEzOC4wNiAxNy4wMkwxMzguMDYgMTguMTlMMTM0LjU2IDE4LjE5TDEzNC41NiAyMC44MkwxMzguNjUgMjAuODJMMTM4LjY1IDIyWk0xNDQuNTMgMTQuNjZMMTQxLjg5IDE0LjY2TDE0MS44OSAxMy40N0wxNDguNjYgMTMuNDdMMTQ4LjY2IDE0LjY2TDE0Ni4wMCAxNC42NkwxNDYuMDAgMjJMMTQ0LjUzIDIyTDE0NC41MyAxNC42NlpNMTUzLjkwIDIyTDE1Mi40MiAyMkwxNTIuNDIgMTMuNDdMMTUzLjkwIDEzLjQ3TDE1My45MCAxNy4wMkwxNTcuNzEgMTcuMDJMMTU3LjcxIDEzLjQ3TDE1OS4xOSAxMy40N0wxNTkuMTkgMjJMMTU3LjcxIDIyTDE1Ny43MSAxOC4yMUwxNTMuOTAgMTguMjFMMTUzLjkwIDIyWk0xNjkuNTEgMjJMMTYzLjkzIDIyTDE2My45MyAxMy40N0wxNjkuNDcgMTMuNDdMMTY5LjQ3IDE0LjY2TDE2NS40MSAxNC42NkwxNjUuNDEgMTcuMDJMMTY4LjkyIDE3LjAyTDE2OC45MiAxOC4xOUwxNjUuNDEgMTguMTlMMTY1LjQxIDIwLjgyTDE2OS41MSAyMC44MkwxNjkuNTEgMjJaTTE3NS4xOSAyMkwxNzMuNzAgMjJMMTczLjcwIDEzLjQ3TDE3Ni43MCAxMy40N1ExNzguMTggMTMuNDcgMTc4Ljk4IDE0LjEzUTE3OS43OSAxNC43OSAxNzkuNzkgMTYuMDVMMTc5Ljc5IDE2LjA1UTE3OS43OSAxNi45MCAxNzkuMzcgMTcuNDhRMTc4Ljk2IDE4LjA2IDE3OC4yMiAxOC4zN0wxNzguMjIgMTguMzdMMTgwLjE0IDIxLjkyTDE4MC4xNCAyMkwxNzguNTUgMjJMMTc2Ljg0IDE4LjcxTDE3NS4xOSAxOC43MUwxNzUuMTkgMjJaTTE3NS4xOSAxNC42NkwxNzUuMTkgMTcuNTJMMTc2LjcxIDE3LjUyUTE3Ny40NiAxNy41MiAxNzcuODggMTcuMTVRMTc4LjMwIDE2Ljc3IDE3OC4zMCAxNi4xMUwxNzguMzAgMTYuMTFRMTc4LjMwIDE1LjQzIDE3Ny45MSAxNS4wNVExNzcuNTIgMTQuNjggMTc2Ljc1IDE0LjY2TDE3Ni43NSAxNC42NkwxNzUuMTkgMTQuNjZaIiBmaWxsPSIjRkZGRkZGIi8+PHBhdGggY2xhc3M9InN2Z19fdGV4dCIgZD0iTTIwOC45NSAyMkwyMDYuMjIgMTMuNjBMMjA4LjY3IDEzLjYwTDIxMC4zNiAxOC45NkwyMTIuMTQgMTMuNjBMMjE0LjMyIDEzLjYwTDIxNi4wMSAxOS4wMUwyMTcuNzggMTMuNjBMMjIwLjA1IDEzLjYwTDIxNy4zMiAyMkwyMTQuNzggMjJMMjEzLjE3IDE2Ljg5TDIxMS40OSAyMkwyMDguOTUgMjJaTTIyNi45NCAyMkwyMjQuNTYgMjJMMjI0LjU2IDEzLjYwTDIyNi45NCAxMy42MEwyMjYuOTQgMjJaTTIzMy45MCAxNS40OEwyMzEuMzIgMTUuNDhMMjMxLjMyIDEzLjYwTDIzOC44NCAxMy42MEwyMzguODQgMTUuNDhMMjM2LjI4IDE1LjQ4TDIzNi4yOCAyMkwyMzMuOTAgMjJMMjMzLjkwIDE1LjQ4Wk0yNDUuNTkgMjJMMjQzLjIxIDIyTDI0My4yMSAxMy42MEwyNDUuNTkgMTMuNjBMMjQ1LjU5IDE2Ljc2TDI0OC44MyAxNi43NkwyNDguODMgMTMuNjBMMjUxLjIxIDEzLjYwTDI1MS4yMSAyMkwyNDguODMgMjJMMjQ4LjgzIDE4LjcyTDI0NS41OSAxOC43MkwyNDUuNTkgMjJaTTI2Ny4zMSAyMkwyNjMuMzQgMjJMMjYzLjM0IDEzLjYwTDI2Ny4zMSAxMy42MFEyNjguNzAgMTMuNjAgMjY5Ljc2IDE0LjEyUTI3MC44MyAxNC42MyAyNzEuNDIgMTUuNThRMjcyLjAxIDE2LjUzIDI3Mi4wMSAxNy44MEwyNzIuMDEgMTcuODBRMjcyLjAxIDE5LjA3IDI3MS40MiAyMC4wMlEyNzAuODMgMjAuOTcgMjY5Ljc2IDIxLjQ4UTI2OC43MCAyMiAyNjcuMzEgMjJMMjY3LjMxIDIyWk0yNjUuNzIgMTUuNTBMMjY1LjcyIDIwLjEwTDI2Ny4yMiAyMC4xMFEyNjguMzAgMjAuMTAgMjY4Ljk1IDE5LjQ5UTI2OS42MCAxOC44OCAyNjkuNjAgMTcuODBMMjY5LjYwIDE3LjgwUTI2OS42MCAxNi43MiAyNjguOTUgMTYuMTFRMjY4LjMwIDE1LjUwIDI2Ny4yMiAxNS41MEwyNjcuMjIgMTUuNTBMMjY1LjcyIDE1LjUwWk0yNzYuNjYgMTguMjZMMjc2LjY2IDE4LjI2TDI3Ni42NiAxMy42MEwyNzkuMDQgMTMuNjBMMjc5LjA0IDE4LjE5UTI3OS4wNCAyMC4yMCAyODAuNjQgMjAuMjBMMjgwLjY0IDIwLjIwUTI4Mi4yMiAyMC4yMCAyODIuMjIgMTguMTlMMjgyLjIyIDE4LjE5TDI4Mi4yMiAxMy42MEwyODQuNTYgMTMuNjBMMjg0LjU2IDE4LjI2UTI4NC41NiAyMC4xMyAyODMuNTIgMjEuMTVRMjgyLjQ4IDIyLjE3IDI4MC42MSAyMi4xN0wyODAuNjEgMjIuMTdRMjc4Ljc0IDIyLjE3IDI3Ny43MCAyMS4xNVEyNzYuNjYgMjAuMTMgMjc2LjY2IDE4LjI2Wk0yODkuMjIgMTcuODBMMjg5LjIyIDE3LjgwUTI4OS4yMiAxNi41NCAyODkuODIgMTUuNTRRMjkwLjQyIDE0LjU1IDI5MS40NyAxMy45OVEyOTIuNTIgMTMuNDMgMjkzLjg0IDEzLjQzTDI5My44NCAxMy40M1EyOTQuOTkgMTMuNDMgMjk1LjkyIDEzLjg0UTI5Ni44NCAxNC4yNSAyOTcuNDUgMTUuMDJMMjk3LjQ1IDE1LjAyTDI5NS45NCAxNi4zOVEyOTUuMTMgMTUuNDAgMjkzLjk2IDE1LjQwTDI5My45NiAxNS40MFEyOTMuMjggMTUuNDAgMjkyLjc0IDE1LjcwUTI5Mi4yMSAxNiAyOTEuOTEgMTYuNTRRMjkxLjYyIDE3LjA5IDI5MS42MiAxNy44MEwyOTEuNjIgMTcuODBRMjkxLjYyIDE4LjUxIDI5MS45MSAxOS4wNVEyOTIuMjEgMTkuNjAgMjkyLjc0IDE5LjkwUTI5My4yOCAyMC4yMCAyOTMuOTYgMjAuMjBMMjkzLjk2IDIwLjIwUTI5NS4xMyAyMC4yMCAyOTUuOTQgMTkuMjJMMjk1Ljk0IDE5LjIyTDI5Ny40NSAyMC41OFEyOTYuODQgMjEuMzUgMjk1LjkyIDIxLjc2UTI5NC45OSAyMi4xNyAyOTMuODQgMjIuMTdMMjkzLjg0IDIyLjE3UTI5Mi41MiAyMi4xNyAyOTEuNDcgMjEuNjFRMjkwLjQyIDIxLjA1IDI4OS44MiAyMC4wNVEyODkuMjIgMTkuMDYgMjg5LjIyIDE3LjgwWk0zMDMuNzggMTUuNDhMMzAxLjIwIDE1LjQ4TDMwMS4yMCAxMy42MEwzMDguNzIgMTMuNjBMMzA4LjcyIDE1LjQ4TDMwNi4xNSAxNS40OEwzMDYuMTUgMjJMMzAzLjc4IDIyTDMwMy43OCAxNS40OFpNMzIxLjg2IDE1LjQ4TDMxOS4yNyAxNS40OEwzMTkuMjcgMTMuNjBMMzI2LjgwIDEzLjYwTDMyNi44MCAxNS40OEwzMjQuMjMgMTUuNDhMMzI0LjIzIDIyTDMyMS44NiAyMkwzMjEuODYgMTUuNDhaTTMzMi41OSAyMkwzMzAuMTYgMjJMMzMzLjg3IDEzLjYwTDMzNi4yMSAxMy42MEwzMzkuOTMgMjJMMzM3LjQ2IDIyTDMzNi44MCAyMC4zN0wzMzMuMjUgMjAuMzdMMzMyLjU5IDIyWk0zMzUuMDIgMTUuOTNMMzMzLjk0IDE4LjYxTDMzNi4xMCAxOC42MUwzMzUuMDIgMTUuOTNaTTM0Ni40NiAyMkwzNDQuMDggMjJMMzQ0LjA4IDEzLjYwTDM0Ny45MyAxMy42MFEzNDkuMDYgMTMuNjAgMzQ5LjkwIDEzLjk4UTM1MC43NCAxNC4zNSAzNTEuMjAgMTUuMDZRMzUxLjY2IDE1Ljc2IDM1MS42NiAxNi43MUwzNTEuNjYgMTYuNzFRMzUxLjY2IDE3LjY2IDM1MS4yMCAxOC4zNVEzNTAuNzQgMTkuMDUgMzQ5LjkwIDE5LjQyUTM0OS4wNiAxOS44MCAzNDcuOTMgMTkuODBMMzQ3LjkzIDE5LjgwTDM0Ni40NiAxOS44MEwzNDYuNDYgMjJaTTM0Ni40NiAxNS40N0wzNDYuNDYgMTcuOTNMMzQ3Ljc4IDE3LjkzUTM0OC41MSAxNy45MyAzNDguODggMTcuNjFRMzQ5LjI2IDE3LjI5IDM0OS4yNiAxNi43MUwzNDkuMjYgMTYuNzFRMzQ5LjI2IDE2LjEyIDM0OC44OCAxNS44MFEzNDguNTEgMTUuNDcgMzQ3Ljc4IDE1LjQ3TDM0Ny43OCAxNS40N0wzNDYuNDYgMTUuNDdaTTM2My4xNSAyMkwzNTYuNDEgMjJMMzU2LjQxIDEzLjYwTDM2My4wMCAxMy42MEwzNjMuMDAgMTUuNDRMMzU4Ljc3IDE1LjQ0TDM1OC43NyAxNi44NUwzNjIuNTAgMTYuODVMMzYyLjUwIDE4LjYzTDM1OC43NyAxOC42M0wzNTguNzcgMjAuMTdMMzYzLjE1IDIwLjE3TDM2My4xNSAyMloiIGZpbGw9IiNGRkZGRkYiIHg9IjIwNS42Nzk5OTk5OTk5OTk5OCIvPjwvc3ZnPg==)](https://forthebadge.com)
paper-trading-sim is a game where the goal is to generate the highest returns possible trading real securities and derivatives with simulated funds

[Changelog »](https://github.com/KingRay171/paper-trading-sim/blob/main/CHANGELOG.rst)

What's new in version 1.1
-------------------------
- further optimized portfolio, watchlist, and wallet ui updates
- optimized generation of etf information dialog
- optimized trade handling
- further optimized creation of technical indicator dialog
- added 8 types of scanners to trade ideas dialog
- added Inverse Cramer, Google Trends, and WallStreetBets scanners to trade ideas dialog
- optimized retrieval and parsing of scanner data

