from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Chess.com")

from .chess_api import get_player_stats, get_profile_player

@mcp.tool()
def get_chess_player_profile(username: str):
    """
        Get the public profile for a Chess.com player by username
    """
    return get_profile_player(username)


@mcp.tool()
def get_chess_player_stats(username: str):
    """
        Get the player stats for a Chess.com player by username
    """
    return get_player_stats(username)

def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()