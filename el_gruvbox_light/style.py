from pygments.style import Style
from pygments.token import (
    Comment, Error, Generic, Keyword, Literal, Name, Number, Operator, 
    Punctuation, String, Text, Whitespace
)

class ELGruvboxLight(Style):
    """
    A custom Pygments style for Haskell syntax highlighting using gruvbox-light colors.
    """
    
    # Base style settings - gruvbox-light colors
    background_color = '#f9f5d7'  # bg0_h
    default_style = '#3c3836'     # fg1
    highlight_color = '#ebdbb2'   # bg1
    line_number_color = '#928374' # gray
    line_number_background_color = '#f2e5bc'  # bg0_s
    line_number_special_color = '#3c3836'     # fg1
    line_number_special_background_color = '#ebdbb2'  # bg1
    
    styles = {
        # Basic tokens
        Text:                      '#3c3836',  # fg1
        Whitespace:                '#928374',  # gray
        Error:                     '#cc241d',  # red
        
        # Comments
        Comment:                   '#79740e',  # green
        Comment.Multiline:         '#79740e',  # green
        Comment.Single:            '#928374',  # green
        Comment.Special:           '#928374',  # gray
        Comment.Preproc:           '#79740e',  # green
        
        # Keywords
        Keyword:                   '#9d0006',  # dark red
        Keyword.Constant:          '#9d0006',  # dark red
        Keyword.Declaration:       '#9d0006',  # dark red
        Keyword.Namespace:         '#9d0006',  # dark red
        Keyword.Pseudo:            '#9d0006',  # dark red
        Keyword.Reserved:          '#9d0006',  # dark red
        Keyword.Type:              '#8f3f71',  # purple
        
        # Names
        Name:                      '#3c3836',  # fg1
        Name.Attribute:            '#af3a03',  # orange
        Name.Builtin:              '#076678',  # blue
        Name.Builtin.Pseudo:       '#076678',  # blue
        Name.Class:                '#8f3f71',  # yellow
        Name.Constant:             '#8f3f71',  # purple
        Name.Decorator:            '#af3a03',  # orange
        Name.Entity:               '#af3a03',  # orange
        Name.Exception:            '#cc241d',  # red
        Name.Function:             '#3c3836',  # fg1
        Name.Label:                '#3c3836',  # fg1
        Name.Namespace:            '#076678',  # blue
        Name.Other:                '#3c3836',  # fg1
        Name.Property:             '#3c3836',  # fg1
        Name.Tag:                  '#076678',  # blue
        Name.Variable:             '#3c3836',  # fg1
        Name.Variable.Class:       '#3c3836',  # fg1
        Name.Variable.Global:      '#3c3836',  # fg1
        Name.Variable.Instance:    '#3c3836',  # fg1

        # Numbers
        Number:                    '#3c3836',  # fg1
        Number.Float:              '#3c3836',  # fg1
        Number.Hex:                '#3c3836',  # fg1
        Number.Integer:            '#3c3836',  # fg1
        Number.Integer.Long:       '#3c3836',  # fg1
        Number.Oct:                '#3c3836',  # fg1
        
        # Operators
        Operator:                  '#076678',  # blue
        Operator.Word:             '#076678',  # blue
        
        # Punctuation
        Punctuation:               '#3c3836',  # fg1
        
        # Strings
        String:                    '#79740e',  # green
        String.Backtick:           '#79740e',  # green
        String.Char:               '#79740e',  # green
        String.Doc:                '#928374',  # gray
        String.Double:             '#79740e',  # green
        String.Escape:             '#af3a03',  # orange
        String.Heredoc:            '#79740e',  # green
        String.Interpol:           '#79740e',  # green
        String.Other:              '#79740e',  # green
        String.Regex:              '#79740e',  # green
        String.Single:             '#79740e',  # green
        String.Symbol:             '#79740e',  # green
        
        # Literals
        Literal:                   '#076678',  # blue
        Literal.Date:              '#79740e',  # green
        
        # Generic tokens (for diffs, etc.)
        Generic:                   '#3c3836',  # fg1
        Generic.Deleted:           '#cc241d',  # red
        Generic.Emph:              '#3c3836',  # fg1
        Generic.Error:             '#cc241d',  # red
        Generic.Heading:           '#3c3836',  # fg1
        Generic.Inserted:          '#79740e',  # green
        Generic.Output:            '#3c3836',  # fg1
        Generic.Prompt:            '#3c3836',  # fg1
        Generic.Strong:            '#3c3836',  # fg1
        Generic.Subheading:        '#3c3836',  # fg1
        Generic.Traceback:         '#076678',  # blue
    }
