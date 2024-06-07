#!python3


import pandocfilters as pf


def wrap_equation(key, value, format, meta):
    if key == "RawBlock" and value[0] == "latex":
        latex_content = value[1]
        if latex_content.startswith(r"\begin{equation}") and latex_content.endswith(
            r"\end{equation}"
        ):
            wrapped_content = "$$" + latex_content + "$$"
            return pf.RawBlock("latex", wrapped_content)


if __name__ == "__main__":
    pf.toJSONFilter(wrap_equation)
