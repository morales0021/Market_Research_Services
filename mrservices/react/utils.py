def generate_hsl_colors(n):
    """
    Generate a list of HSL color strings evenly spaced by hue.
    
    Args:
        n (int): Number of colors to generate.

    Returns:
        List[str]: List of HSL color strings like 'hsl(0, 70%, 50%)'.
    """
    colors = []
    for i in range(n):
        hue = int((360 / n) * i)
        saturation = 70  # You can change this if needed
        lightness = 50   # You can change this too
        colors.append(f"hsl({hue}, {saturation}%, {lightness}%)")
    return colors