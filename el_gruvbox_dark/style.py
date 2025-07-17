from pygments.style import Style
from pygments.token import (
    Comment, Error, Generic, Keyword, Literal, Name, Number, Operator, 
    Punctuation, String, Text, Whitespace
)

class ELGruvboxDark(Style):
    """
    A custom Pygments style for Haskell syntax highlighting using gruvbox-dark colors.
    """
    
    # Base style settings - gruvbox-light colors
    background_color = '#282828'  # bg
    default_style = '#282828'     # bg
    highlight_color = '#ebdbb2'   # fg
    line_number_color = '#282828' # bg
    line_number_background_color = '#282828'  # bg0_s
    line_number_special_color = '#ebdbb2'     # fg
    line_number_special_background_color = '#282828'  # bg
    
    styles = {
        # Basic tokens
        Text:                      '#ebdbb2',  # fg
        Whitespace:                '#928374',  # gray
        Error:                     '#cc241d',  # red
        
        # Comments
        Comment:                   '#98971a',  # green
        Comment.Multiline:         '#98971a',  # green
        Comment.Single:            '#928374',  # green
        Comment.Special:           '#928374',  # gray
        Comment.Preproc:           '#79740e',  # green
        
        # Keywords
        Keyword:                   '#cc241d',  # dark red
        Keyword.Constant:          '#cc241d',  # dark red
        Keyword.Declaration:       '#cc241d',  # dark red
        Keyword.Namespace:         '#cc241d',  # dark red
        Keyword.Pseudo:            '#cc241d',  # dark red
        Keyword.Reserved:          '#cc241d',  # dark red
        Keyword.Type:              '#cc241d',  # dark red
        
        # Names
        Name:                      '#ebdbb2',  # fg
        Name.Attribute:            '#af3a03',  # orange
        Name.Builtin:              '#458588',  # blue
        Name.Builtin.Pseudo:       '#458588',  # blue
        Name.Class:                '#8f3f71',  # yellow
        Name.Constant:             '#8f3f71',  # purple
        Name.Decorator:            '#af3a03',  # orange
        Name.Entity:               '#af3a03',  # orange
        Name.Exception:            '#cc241d',  # red
        Name.Function:             '#3c3836',  # fg
        Name.Label:                '#3c3836',  # fg
        Name.Namespace:            '#458588',  # blue
        Name.Other:                '#3c3836',  # fg
        Name.Property:             '#3c3836',  # fg
        Name.Tag:                  '#458588',  # blue
        Name.Variable:             '#3c3836',  # fg
        Name.Variable.Class:       '#3c3836',  # fg
        Name.Variable.Global:      '#3c3836',  # fg
        Name.Variable.Instance:    '#3c3836',  # fg

        # Numbers
        Number:                    '#ebdbb2',  # fg
        Number.Float:              '#ebdbb2',  # fg
        Number.Hex:                '#ebdbb2',  # fg
        Number.Integer:            '#ebdbb2',  # fg
        Number.Integer.Long:       '#ebdbb2',  # fg
        Number.Oct:                '#ebdbb2',  # fg
        
        # Operators
        Operator:                  '#458588',  # blue
        Operator.Word:             '#458588',  # blue
        
        # Punctuation
        Punctuation:               '#ebdbb2',  # fg
        
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
        Literal:                   '#458588',  # blue
        Literal.Date:              '#79740e',  # green
        
        # Generic tokens (for diffs, etc.)
        Generic:                   '#ebdbb2',  # fg
        Generic.Deleted:           '#cc241d',  # red
        Generic.Emph:              '#3c3836',  # fg
        Generic.Error:             '#cc241d',  # red
        Generic.Heading:           '#3c3836',  # fg
        Generic.Inserted:          '#79740e',  # green
        Generic.Output:            '#3c3836',  # fg
        Generic.Prompt:            '#3c3836',  # fg
        Generic.Strong:            '#3c3836',  # fg
        Generic.Subheading:        '#3c3836',  # fg
        Generic.Traceback:         '#458588',  # blue
    }
